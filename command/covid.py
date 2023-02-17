import requests
from action.sendMessage import sendMessage
from action.seen import seen
def covid(sender_id, message):
    seen(sender_id)
    datacv = requests.get(
    'https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true'
    ).json()
    tc = f'Tổng cộng từ trước tới nay\nCa nhiễm: {str(datacv["infected"])}\n Hồi phục: {str(datacv["recovered"])}\n Điều trị: {str(datacv["treated"])}\n Tử vong: {str(datacv["died"])}\n_______________\n'
    tk = f'Trong ngày\nCa nhiễm mới: {str(datacv["infectedToday"])}\nHồi phục: {str(datacv["recoveredToday"])}\nĐiều trị: {str(datacv["treatedToday"])}\nTử vong: {str(datacv["diedToday"])}'
    sendMessage(sender_id, tc+tk)