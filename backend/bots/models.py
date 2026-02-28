from django.db import models
from django.conf import settings

class TelegramBot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bots')
    token = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    webhook_url = models.URLField(blank=True, null=True)
    webhook_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # WhatsApp Cloud API fields
    whatsapp_phone_number_id = models.CharField(max_length=100, blank=True, null=True, help_text="WhatsApp Phone Number ID from Meta")
    whatsapp_access_token = models.TextField(blank=True, null=True, help_text="WhatsApp Cloud API access token")
    whatsapp_enabled = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.token[:10]

class KnowledgeItem(models.Model):
    TYPE_CHOICES = (
        ('faq', 'FAQ'),
        ('file', 'File'),
        ('text', 'Text Content'),
    )
    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE, related_name='knowledge_items')
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='faq')
    
    # For FAQ/Text
    title = models.CharField(max_length=255, blank=True, help_text="Question or Topic")
    content = models.TextField(blank=True, help_text="Answer or Content")
    
    # For File
    file = models.FileField(upload_to='knowledge/', blank=True, null=True)
    
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Item {self.id}"
