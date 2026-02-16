from rest_framework import viewsets, permissions, filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return conversations for bots owned by the user
        return Conversation.objects.filter(bot__user=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Message.objects.filter(conversation__bot__user=self.request.user).order_by('created_at')
        conversation_id = self.request.query_params.get('conversation')
        if conversation_id:
            queryset = queryset.filter(conversation_id=conversation_id)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.sender == 'admin':
            from bots.services import TelegramService
            try:
                TelegramService.send_message(instance.conversation.bot.token, instance.conversation.telegram_chat_id, instance.content)
            except Exception as e:
                print(f"Failed to send to Telegram: {e}")
