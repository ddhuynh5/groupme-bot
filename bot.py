import requests
import os
from flask import Flask, request
from groupy import Client

token = os.getenv("TOKEN")
bot_id = os.getenv("BOT_ID")
app = Flask(__name__)

client = Client.from_token(token)
group = 90490339
for member in group.members:
    print(member.nickname)


@app.route('/', methods=['GET'])
def home():
    return 'https://my-groupme-bot.onrender.com/'


@app.route('/', methods=['POST'])
def receive():
    print("Incoming Msg: ")
    print(data)

    # Prevent self-reply
    if data['sender_type'] != 'bot':
        if data['text'].startswith('/ping'):
            send(data['name'] + ' pinged me!')

    return 'ok', 200


def send(msg):
    url = "https://api.groupme.com/v3/bots/post"
    json = {
        "bot_id": bot_id,
        "text": msg
    }
    req = requests.post(url, json=json)
    print(req)
