import requests, json
from action.sendMessage import sendMessage
from action.seen import seen


#api sim lỏ hẹo rồi :<
def other(sender_id, message):
  seen(sender_id)
  sendMessage(
    sender_id,
    'Chào bạn đẹp trai đẹp gái gì đó trước màn hình. Vui lòng dùng lệnh "/help" để biết cách sử dụng nhé!!!!!!!'
  )
