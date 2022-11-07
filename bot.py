import requests
from flask import Flask


def create_app():
    app = Flask(__name__)

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
        data = {
            "bot_id": os.getenv("BOT_ID"),
            "text": msg
        }
        req = requests.post(url, data=data)
        print(req)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
