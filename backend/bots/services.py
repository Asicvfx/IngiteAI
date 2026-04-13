import json
import os
import time
from datetime import datetime

import requests
from openai import OpenAI


OPENAI_PRICING = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4.1-mini": {"input": 0.40, "output": 1.60},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
}


def estimate_openai_cost(model, input_tokens, output_tokens):
    pricing = OPENAI_PRICING.get(model)
    if not pricing or input_tokens is None or output_tokens is None:
        return None
    return (input_tokens * pricing["input"] + output_tokens * pricing["output"]) / 1_000_000


class EvalioService:
    TIMEOUT_SECONDS = 20

    @staticmethod
    def is_enabled():
        return bool(
            os.getenv("EVALIO_API_KEY")
            and os.getenv("EVALIO_EXPERIMENT_ID")
            and os.getenv("EVALIO_API_BASE")
        )

    @staticmethod
    def missing_env_keys():
        required = ["EVALIO_API_KEY", "EVALIO_EXPERIMENT_ID", "EVALIO_API_BASE"]
        return [key for key in required if not os.getenv(key)]

    @staticmethod
    def create_client(openai_api_key):
        missing_keys = EvalioService.missing_env_keys()
        if missing_keys:
            print(f"Evalio disabled: missing env vars {missing_keys}")
            return None
        print(
            "Evalio enabled: using embedded adapter "
            f"for experiment {os.getenv('EVALIO_EXPERIMENT_ID')} "
            f"against {os.getenv('EVALIO_API_BASE')}"
        )
        return {
            "api_key": os.getenv("EVALIO_API_KEY", ""),
            "base_url": os.getenv("EVALIO_API_BASE", "").rstrip("/"),
            "openai_api_key": openai_api_key,
        }

    @staticmethod
    def request_variant(client_config, user_id, idempotency_key):
        payload = {
            "experiment_id": int(os.getenv("EVALIO_EXPERIMENT_ID")),
            "user_id": user_id,
        }
        if idempotency_key:
            payload["idempotency_key"] = idempotency_key

        response = requests.post(
            f"{client_config['base_url']}/api/sdk/v1/request/",
            json=payload,
            headers={"X-API-Key": client_config["api_key"]},
            timeout=EvalioService.TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def report_completion(client_config, request_id, usage, latency_ms, cost_usd):
        payload = {
            "request_id": request_id,
            "status": "success",
        }
        if usage:
            if getattr(usage, "prompt_tokens", None) is not None:
                payload["input_tokens"] = usage.prompt_tokens
            if getattr(usage, "completion_tokens", None) is not None:
                payload["output_tokens"] = usage.completion_tokens
        if latency_ms is not None:
            payload["latency_ms"] = latency_ms
        if cost_usd is not None:
            payload["cost_usd"] = f"{cost_usd:.6f}"

        response = requests.post(
            f"{client_config['base_url']}/api/sdk/v1/complete/",
            json=payload,
            headers={"X-API-Key": client_config["api_key"]},
            timeout=EvalioService.TIMEOUT_SECONDS,
        )
        if not response.ok:
            print(
                "Evalio complete failed: "
                f"status={response.status_code}, body={response.text}, payload={payload}"
            )
            response.raise_for_status()
        return payload

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
    def generate_response(
        message_text,
        history=None,
        knowledge_items=None,
        image_url=None,
        user_id=None,
        idempotency_key=None,
    ):
        """
        Generates a highly intelligent response using OpenAI GPT-4o.
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return {"answer": "Error: Neural Core offline. (API Key missing)", "needs_human": True, "lead_type": "cold"}
            
        client = OpenAI(api_key=api_key)

        # Default to the current premium baseline.
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

        if user_id and idempotency_key:
            print(
                "Evalio candidate request: "
                f"user_id={user_id}, idempotency_key={idempotency_key}, "
                f"embedded_adapter=True, enabled={EvalioService.is_enabled()}"
            )
            evalio_client = EvalioService.create_client(api_key)
            if evalio_client:
                try:
                    route_data = EvalioService.request_variant(
                        evalio_client,
                        user_id=user_id,
                        idempotency_key=idempotency_key,
                    )
                    request_id = route_data["request_id"]
                    variant = route_data["variant"]
                    variant_provider = variant["provider"]
                    variant_model = variant["model_name"]
                    variant_name = variant["name"]
                    variant_system_prompt = variant.get("system_prompt", "")
                    variant_extra_params = dict(variant.get("extra_params", {}))
                    print(
                        "Evalio route received: "
                        f"request_id={request_id}, variant={variant_name}, "
                        f"provider={variant_provider}, model={variant_model}"
                    )
                    if variant_provider != "openai":
                        raise ValueError(
                            f"Embedded IngiteAI adapter currently supports only openai variants, got {variant_provider}"
                        )

                    model = variant_model
                    model_messages = list(messages)
                    if variant_system_prompt:
                        model_messages = [{"role": "system", "content": variant_system_prompt}] + model_messages

                    provider_params = {
                        "response_format": {"type": "json_object"},
                        "temperature": 0.2,
                    }
                    provider_params.update(variant_extra_params)

                    start = time.time()
                    response = client.chat.completions.create(
                        model=model,
                        messages=model_messages,
                        **provider_params,
                    )
                    latency_ms = int((time.time() - start) * 1000)
                    usage = getattr(response, "usage", None)
                    input_tokens = getattr(usage, "prompt_tokens", None) if usage else None
                    output_tokens = getattr(usage, "completion_tokens", None) if usage else None
                    cost_usd = estimate_openai_cost(model, input_tokens, output_tokens)
                    EvalioService.report_completion(
                        evalio_client,
                        request_id=request_id,
                        usage=usage,
                        latency_ms=latency_ms,
                        cost_usd=cost_usd,
                    )
                    print(
                        "Evalio completion reported: "
                        f"request_id={request_id}, variant={variant_name}, model={model}"
                    )
                    parsed = json.loads(response.choices[0].message.content)
                    parsed["_evalio"] = {
                        "request_id": request_id,
                        "variant": variant_name,
                        "model": model,
                        "latency_ms": latency_ms,
                        "cost_usd": cost_usd,
                    }
                    return parsed
                except Exception as e:
                    if "request_id" in locals() and "response" in locals():
                        print(
                            "Evalio complete/reporting failed after provider success; "
                            "returning original model output without retrying provider"
                        )
                        parsed = json.loads(response.choices[0].message.content)
                        parsed["_evalio"] = {
                            "request_id": request_id,
                            "variant": variant_name if "variant_name" in locals() else "unknown",
                            "model": model,
                            "latency_ms": latency_ms if "latency_ms" in locals() else None,
                            "cost_usd": cost_usd if "cost_usd" in locals() else None,
                            "reporting_error": str(e),
                        }
                        return parsed
                    print(f"Evalio embedded path failed, falling back to direct OpenAI: {e}")
            else:
                print("Evalio client was not created; using direct OpenAI fallback")
        else:
            print(
                "Evalio skipped: missing stable IDs "
                f"user_id_present={bool(user_id)} idempotency_key_present={bool(idempotency_key)}"
            )

        try:
            start = time.time()
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.2 # Lower temperature for higher reliability
            )
            latency_ms = int((time.time() - start) * 1000)

            parsed = json.loads(response.choices[0].message.content)
            usage = getattr(response, "usage", None)
            input_tokens = getattr(usage, "prompt_tokens", None) if usage else None
            output_tokens = getattr(usage, "completion_tokens", None) if usage else None
            cost_usd = estimate_openai_cost(model, input_tokens, output_tokens)
            parsed["_evalio"] = {
                "request_id": None,
                "variant": "direct_openai_fallback",
                "model": model,
                "latency_ms": latency_ms,
                "cost_usd": cost_usd,
            }
            return parsed
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
