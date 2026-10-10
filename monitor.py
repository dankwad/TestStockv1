import requests
import os

URL = "https://organicclimbing.com/collections/blemish-seconds-pads/products.json"
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK", "")

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
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json={"content": msg})
else:
    print("Not in stock yet.")
