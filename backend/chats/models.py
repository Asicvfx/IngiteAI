from django.db import models
from django.conf import settings
from bots.models import TelegramBot

class Conversation(models.Model):
    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE, related_name='conversations')
    telegram_chat_id = models.CharField(max_length=100)
    lead_type = models.CharField(max_length=20, default='cold') # cold, warm, hot
    needs_human = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.telegram_chat_id} ({self.bot.name})"

    @property
    def last_message(self):
        return self.messages.order_by('-created_at').first()

class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'User'),
        ('bot', 'Bot'),
        ('admin', 'Admin'), # Business owner
    )
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()
    telegram_message_id = models.CharField(max_length=100, null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True) # For products, quick_replies, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content[:50]}"
