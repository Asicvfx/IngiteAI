from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created_at',)

class ConversationSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer(read_only=True)
    bot_name = serializers.CharField(source='bot.name', read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'bot', 'telegram_chat_id')
