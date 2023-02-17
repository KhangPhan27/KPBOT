from action.sendMessage import sendMessage
import wikipedia
from action.seen import seen
def wiki(sender_id, message):
    seen(sender_id)
    try:
        msg=message[6:len(message)]
        wikipedia.set_lang("vi")
        sendMessage(sender_id, wikipedia.summary(msg))
    except:
        sendMessage(sender_id, "Lỗi: LỖI HỆ THỐNG")