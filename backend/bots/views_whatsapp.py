import json
import os
import tempfile
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from django.http import HttpResponse
from bots.models import TelegramBot
from bots.services import OpenAIService
from bots.services_whatsapp import WhatsAppService
from meetings.services import BookingService
from chats.models import Conversation, Message


class WhatsAppWebhookView(APIView):
    """
    Handles incoming WhatsApp messages via Meta Cloud API webhook.
    
    GET: Webhook verification (challenge-response)
    POST: Incoming messages from WhatsApp users
    """
    permission_classes = [permissions.AllowAny]
    
    # Verify token — must match what you set in Meta dashboard
    VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', 'ingiteai_whatsapp_verify_2024')
    
    def get(self, request):
        """
        Webhook verification endpoint.
        Meta sends a GET request to verify the webhook URL.
        """
        mode = request.query_params.get('hub.mode')
        token = request.query_params.get('hub.verify_token')
        challenge = request.query_params.get('hub.challenge')
        
        if mode == 'subscribe' and token == self.VERIFY_TOKEN:
            print(f"WhatsApp Webhook verified successfully!")
            return HttpResponse(challenge, status=200)
        
        print(f"WhatsApp Webhook verification failed. Token: {token}")
        return HttpResponse('Forbidden', status=403)
    
    def post(self, request):
        """
        Handle incoming WhatsApp messages.
        
        Meta sends a POST request with message data in this structure:
        {
            "object": "whatsapp_business_account",
            "entry": [{
                "changes": [{
                    "value": {
                        "metadata": {"phone_number_id": "..."},
                        "messages": [{
                            "from": "77071234567",
                            "type": "text",
                            "text": {"body": "Hello"},
                            "id": "wamid.xxx"
                        }]
                    }
                }]
            }]
        }
        """
        data = request.data
        
        # Must always return 200 OK to Meta quickly
        if data.get('object') != 'whatsapp_business_account':
            return Response(status=status.HTTP_200_OK)
        
        try:
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    value = change.get('value', {})
                    metadata = value.get('metadata', {})
                    phone_number_id = metadata.get('phone_number_id')
                    
                    messages = value.get('messages', [])
                    if not messages:
                        continue
                    
                    # Find the bot by WhatsApp phone number ID
                    try:
                        bot = TelegramBot.objects.get(
                            whatsapp_phone_number_id=phone_number_id,
                            whatsapp_enabled=True
                        )
                    except TelegramBot.DoesNotExist:
                        print(f"WhatsApp: No bot found for phone_number_id {phone_number_id}")
                        continue
                    
                    for msg in messages:
                        self._process_message(bot, msg, phone_number_id)
        
        except Exception as e:
            print(f"WhatsApp webhook error: {e}")
        
        return Response(status=status.HTTP_200_OK)
    
    def _process_message(self, bot, msg, phone_number_id):
        """Process a single WhatsApp message."""
        msg_type = msg.get('type')
        sender_phone = msg.get('from')  # e.g. "77071234567"
        msg_id = msg.get('id')
        
        text = ''
        image_url = None
        
        # Handle text messages
        if msg_type == 'text':
            text = msg.get('text', {}).get('body', '')
        
        # Handle image messages
        elif msg_type == 'image':
            image_data = msg.get('image', {})
            caption = image_data.get('caption', '')
            media_id = image_data.get('id')
            
            if media_id:
                # Get image URL from Meta
                media_url = WhatsAppService.get_media_url(
                    bot.whatsapp_access_token, media_id
                )
                if media_url:
                    image_url = media_url
            
            text = caption or "[User sent an image]"
        
        # Handle voice/audio messages
        elif msg_type in ('audio', 'voice'):
            audio_data = msg.get(msg_type, {})
            media_id = audio_data.get('id')
            
            if media_id:
                media_url = WhatsAppService.get_media_url(
                    bot.whatsapp_access_token, media_id
                )
                if media_url:
                    # Download and transcribe
                    audio_content = WhatsAppService.download_media(
                        bot.whatsapp_access_token, media_url
                    )
                    if audio_content:
                        try:
                            with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp:
                                tmp.write(audio_content)
                                tmp_path = tmp.name
                            
                            transcription = OpenAIService.transcribe_audio(tmp_path)
                            if transcription:
                                text = transcription
                            os.remove(tmp_path)
                        except Exception as e:
                            print(f"WhatsApp voice processing error: {e}")
                            text = "[Voice transcription failed]"
            
            if not text:
                text = "[Voice message]"
        
        # Handle location messages
        elif msg_type == 'location':
            loc = msg.get('location', {})
            lat = loc.get('latitude')
            lng = loc.get('longitude')
            text = f"📍 Location: {lat}, {lng}"
        
        # Handle interactive button replies
        elif msg_type == 'interactive':
            interactive = msg.get('interactive', {})
            if interactive.get('type') == 'button_reply':
                text = interactive.get('button_reply', {}).get('title', '')
            elif interactive.get('type') == 'list_reply':
                text = interactive.get('list_reply', {}).get('title', '')
        
        else:
            text = f"[Unsupported message type: {msg_type}]"
        
        if not text and not image_url:
            return
        
        # Mark as read (blue ticks)
        WhatsAppService.mark_as_read(
            phone_number_id, bot.whatsapp_access_token, msg_id
        )
        
        # Get or Create Conversation (platform = whatsapp)
        conversation, created = Conversation.objects.get_or_create(
            bot=bot,
            telegram_chat_id=sender_phone,
            platform='whatsapp'
        )
        
        # Save User Message
        Message.objects.create(
            conversation=conversation,
            sender='user',
            content=text,
            telegram_message_id=msg_id
        )
        
        # Prepare History
        history_messages = Message.objects.filter(
            conversation=conversation
        ).order_by('-created_at')[:10]
        
        history = []
        for m in reversed(list(history_messages)):
            role = 'user' if m.sender == 'user' else 'assistant'
            history.append({"role": role, "content": m.content})
        
        # Generate AI Response
        knowledge_items = bot.knowledge_items.all()
        print(f"WhatsApp: Processing message from {sender_phone}: {text[:50]}...")
        ai_response = OpenAIService.generate_response(
            text, history=history, knowledge_items=knowledge_items, image_url=image_url
        )
        print(f"WhatsApp: AI Response: {ai_response}")
        
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
        
        # Save Bot Message and Send to WhatsApp
        answer_text = ai_response.get('answer', '')
        if answer_text:
            metadata = {
                "products": ai_response.get('products', []),
                "quick_replies": ai_response.get('quick_replies', [])
            }
            Message.objects.create(
                conversation=conversation,
                sender='bot',
                content=answer_text,
                metadata=metadata
            )
            
            # Send via WhatsApp
            print(f"WhatsApp: Sending reply to {sender_phone}")
            result = WhatsAppService.send_message(
                phone_number_id,
                bot.whatsapp_access_token,
                sender_phone,
                answer_text
            )
            print(f"WhatsApp: Send result: {result}")
