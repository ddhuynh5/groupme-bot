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
        if data['text'].startswith('test') and data['name'] == 'Dennis Huynh':
            send('Hello ' + data['name'])
        if data['text'].startswith('ayo'):
            send('The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')

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
