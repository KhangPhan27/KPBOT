import requests, json
from config import config
PAGE_ACCESS_TOKEN=config["PAGE_ACCESS_TOKEN"]
def sendMessage(sender_id,message_text):
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
        "id": sender_id
    },
        "message": {
        "text": message_text
    }
    })
    requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)
    