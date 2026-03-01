import requests
import json
import os


class WhatsAppService:
    """
    Service for Meta WhatsApp Cloud API.
    Handles sending messages and verifying webhooks.
    """
    
    GRAPH_API_URL = "https://graph.facebook.com/v22.0"
    
    @staticmethod
    def send_message(phone_number_id, access_token, to, text):
        """
        Send a text message via WhatsApp Cloud API.
        phone_number_id: The WhatsApp phone number ID (from Meta dashboard)
        access_token: The WhatsApp access token
        to: Recipient phone number (international format, e.g. 77071234567)
        text: Message text
        """
        # Clean up token and phone number
        access_token = access_token.strip()
        to = to.strip().replace('+', '').replace(' ', '')
        phone_number_id = str(phone_number_id).strip()
        
        url = f"{WhatsAppService.GRAPH_API_URL}/{phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": text
            }
        }
        
        # Debug logging
        print(f"WhatsApp DEBUG: URL={url}")
        print(f"WhatsApp DEBUG: to={to}, phone_id={phone_number_id}")
        print(f"WhatsApp DEBUG: token_start={access_token[:30]}...")
        
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=15)
            result = r.json()
            print(f"WhatsApp send result: {result}")
            return result
        except Exception as e:
            print(f"WhatsApp Send Error: {e}")
            return {"error": str(e)}
    
    @staticmethod
    def mark_as_read(phone_number_id, access_token, message_id):
        """Mark a WhatsApp message as read (blue ticks)."""
        url = f"{WhatsAppService.GRAPH_API_URL}/{phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        try:
            requests.post(url, headers=headers, json=payload, timeout=10)
        except Exception as e:
            print(f"WhatsApp mark_as_read error: {e}")

    @staticmethod
    def get_media_url(access_token, media_id):
        """Get download URL for a WhatsApp media file (image, voice, etc.)."""
        url = f"{WhatsAppService.GRAPH_API_URL}/{media_id}"
        headers = {"Authorization": f"Bearer {access_token}"}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            data = r.json()
            return data.get("url")
        except Exception as e:
            print(f"WhatsApp get_media_url error: {e}")
            return None

    @staticmethod
    def download_media(access_token, media_url):
        """Download media content from WhatsApp."""
        headers = {"Authorization": f"Bearer {access_token}"}
        try:
            r = requests.get(media_url, headers=headers, timeout=30)
            return r.content
        except Exception as e:
            print(f"WhatsApp download_media error: {e}")
            return None
