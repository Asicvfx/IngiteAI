import os

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from django.shortcuts import get_object_or_404
from .services import EvalioService, OpenAIService, TelegramService
from meetings.services import BookingService
from chats.models import Conversation, Message
from .models import TelegramBot, KnowledgeItem
from .serializers import TelegramBotSerializer, KnowledgeItemSerializer

class WebhookView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, token):
        print(f"DEBUG: Webhook received for token {token[:10]}...")
        bot = get_object_or_404(TelegramBot, token=token)
        
        data = request.data
        if 'message' not in data:
            return Response(status=status.HTTP_200_OK)

        msg_data = data['message']
        chat_id = msg_data['chat']['id']
        text = msg_data.get('text', '')
        
        # Multimedia Handling
        image_url = None
        if 'photo' in msg_data:
            # Telegram sends multiple sizes, take the largest
            photo = msg_data['photo'][-1]
            image_url = TelegramService.get_file_url(token, photo['file_id'])
            if not text: text = "[User sent an image]"
            
        if 'voice' in msg_data:
            voice = msg_data['voice']
            voice_url = TelegramService.get_file_url(token, voice['file_id'])
            if voice_url:
                # Download and transcribe
                import tempfile
                try:
                    r = requests.get(voice_url, timeout=15)
                    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp:
                        tmp.write(r.content)
                        tmp_path = tmp.name
                    
                    transcription = OpenAIService.transcribe_audio(tmp_path)
                    if transcription:
                        text = transcription
                    os.remove(tmp_path)
                except Exception as e:
                    print(f"Voice processing error: {e}")
                    text = "[Voice transcription failed]"

        if not text and not image_url:
             return Response(status=status.HTTP_200_OK)

        # Get or Create Conversation
        conversation, created = Conversation.objects.get_or_create(
            bot=bot, 
            telegram_chat_id=str(chat_id)
        )

        # Save User Message
        Message.objects.create(
            conversation=conversation,
            sender='user',
            content=text,
            telegram_message_id=msg_data.get('message_id')
        )

        # Prepare History (excluding the current message we just saved)
        history_messages = Message.objects.filter(conversation=conversation).exclude(content=text).order_by('-created_at')[:10]
        history = []
        for m in reversed(history_messages):
            role = 'user' if m.sender == 'user' else 'assistant'
            history.append({"role": role, "content": m.content})

        # Generate AI Response
        knowledge_items = bot.knowledge_items.all()
        print(f"DEBUG: Calling OpenAIService. Text: {text}, Image: {image_url}")
        message_id = msg_data.get('message_id')
        ai_response = OpenAIService.generate_response(
            text,
            history=history,
            knowledge_items=knowledge_items,
            image_url=image_url,
            user_id=f"telegram:{chat_id}",
            idempotency_key=f"telegram:{chat_id}:{message_id}",
        )
        print(f"DEBUG: AI Response received: {ai_response}")
        
        # Update Conversation Status
        conversation.needs_human = ai_response.get('needs_human', False)
        conversation.lead_type = ai_response.get('lead_type', 'cold')
        conversation.save()

        # Trigger Meeting Booking if requested
        if ai_response.get('booking_requested') and ai_response.get('booking_details'):
            details = ai_response['booking_details']
            BookingService.create_meeting(
                bot=bot,
                conversation=conversation,
                customer_name=details.get('name', 'Lead'),
                customer_email=details.get('email', ''),
                start_time_str=details.get('time', '')
            )

        evalio_meta = ai_response.get('_evalio') or {}
        evalio_request_id = evalio_meta.get('request_id')
        if evalio_request_id and EvalioService.is_enabled():
            evalio_client = EvalioService.create_client(os.getenv('OPENAI_API_KEY'))
            if evalio_client:
                try:
                    if ai_response.get('booking_requested') and ai_response.get('booking_details'):
                        EvalioService.report_feedback(
                            evalio_client,
                            request_id=evalio_request_id,
                            score=1,
                            comment="business_outcome:lead_captured",
                            idempotency_key=f"telegram:{chat_id}:{message_id}:lead-captured",
                        )
                        print(
                            "Evalio feedback reported: "
                            f"request_id={evalio_request_id}, score=1, outcome=lead_captured"
                        )
                    elif ai_response.get('needs_human'):
                        EvalioService.report_feedback(
                            evalio_client,
                            request_id=evalio_request_id,
                            score=-1,
                            comment="business_outcome:manager_handoff",
                            idempotency_key=f"telegram:{chat_id}:{message_id}:manager-handoff",
                        )
                        print(
                            "Evalio feedback reported: "
                            f"request_id={evalio_request_id}, score=-1, outcome=manager_handoff"
                        )
                except Exception as e:
                    print(f"Evalio feedback reporting error: {e}")

        # Save Bot Message
        answer_text = ai_response.get('answer', '')
        if answer_text:
             # Prepare metadata for futuristic UI
             metadata = {
                 "products": ai_response.get('products', []),
                 "quick_replies": ai_response.get('quick_replies', [])
             }
             if ai_response.get('_evalio'):
                 metadata["evalio"] = ai_response["_evalio"]
             Message.objects.create(
                conversation=conversation,
                sender='bot',
                content=answer_text,
                metadata=metadata
             )
             # Send to Telegram
             print(f"DEBUG: Sending message to Telegram chat {chat_id}")
             res = TelegramService.send_message(token, chat_id, answer_text)
             print(f"DEBUG: Telegram response: {res}")

        return Response(status=status.HTTP_200_OK)


class TelegramBotViewSet(viewsets.ModelViewSet):
    serializer_class = TelegramBotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TelegramBot.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class KnowledgeItemViewSet(viewsets.ModelViewSet):
    serializer_class = KnowledgeItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return KnowledgeItem.objects.filter(bot__user=self.request.user)
