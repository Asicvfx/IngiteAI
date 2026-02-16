from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import KnowledgeItem, TelegramBot
from .services_knowledge import KnowledgeService
from .services import TelegramService

@receiver(post_save, sender=KnowledgeItem)
def process_knowledge_file(sender, instance, created, **kwargs):
    """Automatically parse uploaded files for KnowledgeItems."""
    if instance.file and (created or not instance.content):
        # We only parse if it's a file type and has no content yet
        if instance.item_type == 'file' or (not instance.content and instance.file):
            parsed_content = KnowledgeService.extract_text_from_file(instance.file)
            if parsed_content:
                # Update without triggering signal again
                KnowledgeItem.objects.filter(pk=instance.pk).update(content=parsed_content)

@receiver(post_save, sender=TelegramBot)
def setup_bot_webhook(sender, instance, created, **kwargs):
    """Automatically register webhook in Telegram when bot is created or token changed."""
    if created or not instance.webhook_url:
        # Construct webhook URL: PROJECT_URL + /api/v1/bots/webhook/<token>/
        project_url = getattr(settings, 'PROJECT_URL', '').rstrip('/')
        if project_url:
            webhook_url = f"{project_url}/api/v1/bots/webhook/{instance.token}/"
            print(f"DEBUG: Registering webhook for {instance.name}: {webhook_url}")
            
            res = TelegramService.set_webhook(instance.token, webhook_url)
            if res.get('ok'):
                # Update without triggering signal again
                TelegramBot.objects.filter(pk=instance.pk).update(
                    webhook_url=webhook_url,
                    webhook_status=True
                )
            else:
                print(f"DEBUG: Failed to set webhook: {res.get('description')}")
