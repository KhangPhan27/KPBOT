import requests 
from action.sendMessage import sendMessage
from action.seen import seen
def dichv(sender_id, message):
    seen(sender_id)
    msg=message[7:len(message)]
    res = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q={msg}").json()
    res2 = res[0]
    trans = res2[0]
    sendMessage(sender_id,str(trans[0]))