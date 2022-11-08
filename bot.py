import requests
import os
from flask import Flask, request

token = os.getenv("TOKEN")
bot_id = os.getenv("BOT_ID")
app = Flask(__name__)

url = "https://api.groupme.com/v3/bots/post"


@app.route('/', methods=['GET'])
def home():
    return 'https://my-groupme-bot.onrender.com/'


@app.route('/', methods=['POST'])
def receive():
    data = request.get_json()
    print("Incoming Msg: ")
    print(data)

    # Prevent self-reply
    if data['sender_type'] != 'bot':
        if data['text'].startswith('/ping'):
            send(data['name'] + ' pinged me!')
        if data['name'] == "Dennis Huynh" and data['text'].startswith('ayo'):
            send_with_img('hi', 'ayo.jpg')

    return 'ok', 200


def send(msg):
    json = {
        "bot_id": bot_id,
        "text": msg
    }
    req = requests.post(url, json=json)
    print("request: ", req)


def send_with_img(msg, img):
    json = {
        "bot_id": bot_id,
        "text": msg,
        "attachments": [
            {
                "type": "image",
                "url": img
            }
        ]
    }
    req = requests.post(url, json=json)
    print("request: ", req)
