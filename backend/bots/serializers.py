from rest_framework import serializers
from .models import TelegramBot, KnowledgeItem

class KnowledgeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class TelegramBotSerializer(serializers.ModelSerializer):
    knowledge_items = KnowledgeItemSerializer(many=True, read_only=True)

    class Meta:
        model = TelegramBot
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')

    def create(self, validated_data):
        from .services import TelegramService
        validated_data['user'] = self.context['request'].user
        bot = super().create(validated_data)
        
        # We don't know the public URL yet (localhost won't work), 
        # but we can try to set it if we had a BASE_URL setting.
        # For now, just a placeholder for the logic.
        return bot
