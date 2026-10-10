import requests
import os

URL = "https://organicclimbing.com/collections/blemish-seconds-pads/products.json"
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

def check_stock():
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        for product in response.json().get("products", []):
            if "BIG FIVE" in product.get("title", "").upper():
                for variant in product.get("variants", []):
                    if variant.get("available") == True:
                        return True
        return False
    except Exception as e:
        print(f"Error checking stock: {e}")
        return False

if check_stock():
    msg = "🚨 IN STOCK! Blemished Big 5 Pad is available! https://organicclimbing.com/collections/blemish-seconds-pads"
    print(msg)
    
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg
        }
        requests.post(tg_url, json=payload)
else:
    print("Not in stock yet.")
