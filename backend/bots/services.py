import requests
import json
import os
from datetime import datetime
from django.conf import settings
from openai import OpenAI

class OpenAIService:
    @staticmethod
    def transcribe_audio(audio_file_path):
        """Transcribes audio using OpenAI Whisper."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key: return "Transcription failed: No API Key."
        client = OpenAI(api_key=api_key)
        try:
            with open(audio_file_path, "rb") as audio:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio
                )
                return transcript.text
        except Exception as e:
            print(f"Whisper Error: {e}")
            return f"Transcription error: {str(e)}"

    @staticmethod
    def generate_response(message_text, history=None, knowledge_items=None, image_url=None):
        """
        Generates a highly intelligent response using OpenAI GPT-4o.
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return {"answer": "Error: Neural Core offline. (API Key missing)", "needs_human": True, "lead_type": "cold"}
            
        client = OpenAI(api_key=api_key)
        
        # We always use gpt-4o for maximum intelligence in this premium version
        model = "gpt-4o"
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        system_prompt = f"""You are 'IngiteAI Prime', an elite business neural assistant. 
Your personality: Ultra-professional, concise, visionary, and deeply helpful. 
You are NOT a generic chatbot. You are a high-level executive assistant representing a premium brand.

GOALS:
1. Provide exact, data-driven answers from the 'KNOWLEDGE BASE' section below.
2. Convert leads by being proactive but not pushy.
3. Use interactive elements (Product Cards, Quick Replies) to create a futuristic experience.

RULES OF ENGAGEMENT:
- KNOWLEDGE FIRST: If the answer is in the Knowledge Base, use it. If not, politely state you'll escalate to a human expert.
- LINGUISTIC PERSISTENCE: Always respond in the EXACT same language as the user.
- TONE: Maintain a high-end, futuristic tech aesthetic in your language.
- MULTIMEDIA: If an image is provided, analyze it clinically and provide business insights.

INTERACTIVE PROTOCOLS:
- PRODUCTS: If a user asks about pricing, catalog, or specific items, you MUST populate the 'products' array with JSON objects: {{"name": "...", "price": "...", "description": "...", "image_url": "..."}}.
- QUICK REPLIES: Always provide 2-3 logical 'next-step' buttons in the 'quick_replies' array (e.g., ["Book a Demo", "View Pricing", "Technical Specs"]).
- BOOKING: If intent to meet/call is detected, guide them for: Name, Email, DateTime. 
  ONLY set 'booking_requested': true and fill 'booking_details' when you have all 3.

SIMULATED CONTEXT:
- Current Time: {current_time}

OUTPUT FORMAT:
You MUST output valid, structured JSON exactly like this:
{{
    "answer": "Your elegant and informative response in the user's language",
    "needs_human": false,
    "booking_requested": false,
    "booking_details": null,
    "lead_type": "cold/warm/hot",
    "products": [],
    "quick_replies": []
}}
"""
        
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add Knowledge Base with clear structure
        if knowledge_items:
            kb_parts = ["--- START OF KNOWLEDGE BASE ---"]
            for i in knowledge_items:
                title = getattr(i, 'title', 'General Info')
                content = getattr(i, 'content', '')
                if content:
                    kb_parts.append(f"DOCUMENT: {title}\nCONTENT: {content}")
            kb_parts.append("--- END OF KNOWLEDGE BASE ---")
            messages.append({"role": "system", "content": "\n\n".join(kb_parts)})
        
        # Add Conversation History (Deep memory)
        if history:
            # We take up to 15 messages for better context
            for msg in history[-15:]:
                messages.append(msg)
                
        # Handle Multimedia Input
        user_content = []
        if message_text:
            user_content.append({"type": "text", "text": message_text})
        if image_url:
            user_content.append({"type": "image_url", "image_url": {"url": image_url}})
            
        messages.append({"role": "user", "content": user_content if image_url else message_text})

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.2 # Lower temperature for higher reliability
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Neural Failure Trace: {e}")
            return {
                "answer": "System neural failure. I am currently synchronizing with the central grid. Please stand by.",
                "needs_human": True, 
                "lead_type": "cold",
                "products": [],
                "quick_replies": ["Retry Connection"]
            }

class TelegramService:
    @staticmethod
    def get_file_url(token, file_id):
        url = f"https://api.telegram.org/bot{token}/getFile"
        try:
            res = requests.get(url, params={"file_id": file_id}, timeout=10)
            if res.status_code == 200:
                file_path = res.json().get('result', {}).get('file_path')
                if file_path:
                    return f"https://api.telegram.org/file/bot{token}/{file_path}"
        except Exception as e:
            print(f"Telegram getFile error: {e}")
        return None

    @staticmethod
    def send_message(token, chat_id, text):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML" # Enable rich text in Telegram
        }
        try:
            r = requests.post(url, json=payload, timeout=10)
            return r.json()
        except Exception as e:
            print(f"Telegram Send Error: {e}")
            return {"ok": False, "error": str(e)}

    @staticmethod
    def set_webhook(token, url):
        """Registers a webhook URL with Telegram for this bot."""
        telegram_url = f"https://api.telegram.org/bot{token}/setWebhook"
        try:
            res = requests.post(telegram_url, data={"url": url}, timeout=10)
            return res.json()
        except Exception as e:
            print(f"Telegram setWebhook error: {e}")
            return {"ok": False, "error": str(e)}
