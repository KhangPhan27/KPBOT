import openai
from action.sendMessage import sendMessage
from config import config
from action.seen import seen
def gpt(sender_id, message):
            try:
                seen(sender_id)
                msg=message[5:len(message)]
                openai.api_key = config["OPENAI_API"]
                res = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=msg,
                    max_tokens=4000,
                    temperature=0
                )
                res = res.choices[0].text
                sendMessage(sender_id, res)
            except:
                    sendMessage(sender_id, "Lỗi rồi, thử lại nhé!")
