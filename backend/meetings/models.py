from django.db import models
from bots.models import TelegramBot
from chats.models import Conversation

class Meeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE, related_name='meetings')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='meetings')
    customer_name = models.CharField(max_length=255, blank=True)
    customer_email = models.EmailField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    meeting_link = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting with {self.customer_name or 'Lead'} at {self.start_time}"
