"""Quick test - paste your FRESH token from Meta Dashboard"""
import requests

# ВАЖНО: Вставь СВЕЖИЙ токен с Meta Dashboard (нажми Copy)
ACCESS_TOKEN = "EAAM4Lqaji4ABQZCZBH8ZCJiXCajS2ZAkrZCfVHZBvlJj1wANphuCHfKRor6iMWpiMgP9YJhTWzSCctSyW51MaNeMO4oI3nuVQZCDWSV4HLWyZAfVD5FNYUWh0TZBhsX3rdCWTOom9cU64PjZB8ti8wYWv6enfAQJZCcco283WPQlw2IRQ5Qrs2P9BLdlHUKzI7CSxnC0LbOZCHZCrLanzreTONXkcZBSSDCykZBO0MlpBAR91QS3BZCCDfYlYh1V9uQYOZB208OuGKl0uMR2zokXHMmOXMDYpm7HhJAZDZD"

PHONE_NUMBER_ID = "1057605997426895"

url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Test different number formats
numbers_to_try = [
    "77752786692",     # +7 without +
    "787752786692",    # with 8 prefix  
    "+77752786692",    # with +
]

for num in numbers_to_try:
    print(f"\n=== Testing number: {num} ===")
    payload = {
        "messaging_product": "whatsapp",
        "to": num,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }
    }
    r = requests.post(url, headers=headers, json=payload, timeout=15)
    data = r.json()
    if "error" in data:
        print(f"FAIL: {data['error']['message']}")
    else:
        print(f"SUCCESS! {data}")
