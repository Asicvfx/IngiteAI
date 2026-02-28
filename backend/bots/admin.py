from django.contrib import admin
from .models import TelegramBot, KnowledgeItem


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_active', 'whatsapp_enabled', 'created_at')
    list_filter = ('is_active', 'whatsapp_enabled')
    fieldsets = (
        ('Основное', {
            'fields': ('user', 'name', 'token', 'is_active')
        }),
        ('Telegram Webhook', {
            'fields': ('webhook_url', 'webhook_status')
        }),
        ('WhatsApp Cloud API', {
            'fields': ('whatsapp_phone_number_id', 'whatsapp_access_token', 'whatsapp_enabled'),
            'description': 'Данные из Meta Developer Dashboard для WhatsApp интеграции'
        }),
    )


@admin.register(KnowledgeItem)
class KnowledgeItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'bot', 'item_type', 'created_at')
    list_filter = ('item_type',)
