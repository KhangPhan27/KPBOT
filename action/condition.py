import threading
from command.help import help
from command.covid import covid
from command.diche import diche
from command.dichv import dichv
from command.wiki import wiki
from command.fact import fact
from command.sim import sim
from command.gpt import gpt
def condition(sender_id, message_text):
    if any(["/wiki" in message_text.lower()]):
        thread1 = threading.Thread(target=wiki, args=(sender_id, message_text))
        thread1.start()
    elif any(["/help" in message_text.lower()]):
        thread1 = threading.Thread(target=help, args=(sender_id, message_text))
        thread1.start()
    elif any(["/covid" in message_text.lower()]):
        thread1 = threading.Thread(target=covid, args=(sender_id, message_text))
        thread1.start()
    elif any(["/diche" in message_text.lower()]):
        thread1 = threading.Thread(target=diche, args=(sender_id, message_text))
        thread1.start()
    elif any(["/dichv" in message_text.lower()]):
        thread1 = threading.Thread(target=dichv, args=(sender_id, message_text))
        thread1.start()
    elif any(["/fact" in message_text.lower()]):
        thread1 = threading.Thread(target=fact, args=(sender_id, message_text))
        thread1.start()
    elif any(["/gpt" in message_text.lower()]):
        thread1 = threading.Thread(target=gpt, args=(sender_id, message_text))
        thread1.start()
    else:
        thread1 = threading.Thread(target=sim, args=(sender_id, message_text))
        thread1.start()
