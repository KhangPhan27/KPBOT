from action.sendMedia import sendMedia
from action.sendMessage import sendMessage
import requests
from action.seen import seen
def tik(sender_id, message_text):
    seen(sender_id)
    try:
        link= message_text[5:len(message_text)]
        url= 'https://video-nwm.p.rapidapi.com/url/'
        params= { 'url':f"\{link}" }
        headers= {
            'x-rapidapi-key': '6535f33dffmsh5f43874ed2e707fp1231cfjsn409b1e61e094',
            'x-rapidapi-host': 'video-nwm.p.rapidapi.com'
        }
        req=requests.get(url, params=params, headers=headers).json()
        listVideo=req['item']['video']["playAddr"]
        sendMedia(sender_id,"video",listVideo[len(listVideo)-1])
    except:
        sendMessage(sender_id,"Lỗi rồi, thử clip khác nhé!")
