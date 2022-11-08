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
        if data['text'].startswith('ayo'):
            post_img_to_groupme('ayo.jpg')
            send_with_img('ayo', 'ayo.jpg')

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


def post_img_to_groupme(img):
    img_url = 'https://image.groupme.com/pictures'
    json = {
        "access_token": token,
        "attachments": [
            {
                "type": "image",
                "url": img
            }
        ]
    }
    requests.post(img_url, json=json)
