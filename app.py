from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8735369719:AAH1bNNhSn5B70pym_owDZiiHhPOdBRIkvs"
CHAT_ID = "7138645240"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, json=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    signal = data.get("signal", "")
    price = data.get("price", "")

    message = f"""
📊 SIGNAL

Signal: {signal}
Price: {price}
"""
    send_telegram(message)
    return {"ok": True}

@app.route('/')
def home():
    return "Bot is running"
