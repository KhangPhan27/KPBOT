import requests, json
from config import config
PAGE_ACCESS_TOKEN=config["PAGE_ACCESS_TOKEN"]
def seen(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        "recipient": {
        "id": sender_id
    },
         "sender_action": "mark_seen"
    })

    requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)