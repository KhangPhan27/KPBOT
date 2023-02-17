from action.sendMedia import sendMedia
import random
import urllib
import requests
import json
import threading
from action.sendMessage import sendMessage
from action.seen import seen
def img(sender_id, message_text):
    seen(sender_id)
    try:
        content=message_text[5:len(message_text)]
        r = requests.get("https://tr.pinterest.com/resource/BaseSearchResource/get/?",
                        params={"source_url": f"/search/pins/?q="+content, 
                        "data": '''{"options":{"page_size":25,"query":"''' + content + '''","scope":"pins","bookmarks":["''' + "" + '''"],"field_set_key":"unauth_react","no_fetch_context_on_resource":false},"context":{}}'''.strip()})
        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        listURL=[]
        for i in results:
                    listURL.append(i["images"]["orig"]["url"])
        choice=random.choice(listURL)
        sendMedia(sender_id, "image", choice)
    except:
           sendMessage(sender_id, "Lỗi rồi, đổi từ khác nhé!")