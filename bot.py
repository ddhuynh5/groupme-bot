import os
import json
import requests
from flask import Flask, request

token = os.getenv("TOKEN")
bot_id = os.getenv("BOT_ID")
app = Flask(__name__)

url = "https://api.groupme.com/v3/bots/post"
img_url = "https://image.groupme.com"


@app.route("/", methods=["GET"])
def home():
    return "https://my-groupme-bot.onrender.com/"


@app.route("/", methods=["POST"])
def receive():
    data = request.get_json()
    print("Incoming Msg: ")
    print(data)

    # Prevent self-reply
    if data["sender_type"] != "bot":
        if data["text"].startswith("/ping"):
            send(data["name"] + " pinged me!")
        if data["name"] == "Nathan Rolfes":
            send("ok")
        if data["text"].startswith("ayo"):
            send(
                "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")
        if data["text"].startswith("cat"):
            send_cat()
        else:
            post_img_to_groupme()

    return "ok", 200


def send(msg):
    json = {
        "bot_id": bot_id,
        "text": msg
    }
    req = requests.post(url, json=json)
    print("request: ", req)


def send_cat():
    cat_url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(cat_url)
    res = response.json()

    for r in res:
        req = requests.post(cat_url, json=r["url"])
    print("cat: ", req)


def post_img_to_groupme():
    data = open("./mat.jpeg", "rb").read()
    req = requests.post(url, json=data)
    print("HERE: ", req)


def post_img_to_chat(img):
    post_data = {"text": "TESTING TEST TEST RAHHHH",
                 "picture_url": YOUR_PIC_URL}

    requests.post("https://api.groupme.com/v3/bots/post",
                  params=post_params, data=post_data)
