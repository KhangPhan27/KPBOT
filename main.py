import requests
import threading
from flask import Flask, request
from action.sendMessage import sendMessage
from action.condition import condition
from config import config
app = Flask(__name__)
from sanic import response
# Adds support for GET requests to our webhook
@app.route('/', methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== config["VERIFY_TOKEN"]:
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
@app.route("/", methods=['POST'])
def fbwebhook():
   data_user=request.get_json()
   try:
        for event in data_user['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    sender_id = message['sender']['id']
                    message_text = message["message"]["text"]
                    condition(sender_id, message_text)
   except:
       pass
   return "Message Processed"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)