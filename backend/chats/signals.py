from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Message
from .serializers import MessageSerializer

@receiver(post_save, sender=Message)
def broadcast_new_message(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        serializer = MessageSerializer(instance)
        async_to_sync(channel_layer.group_send)(
            "chat_updates",
            {
                "type": "chat_message",
                "message": serializer.data
            }
        )
