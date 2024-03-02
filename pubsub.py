from typing import Callable, Tuple, Any, List
from collections import defaultdict
from threading import Thread
from pydantic import BaseModel
import time
from icecream import ic

# src, topic, message_data -> void
type MessageCB = Callable[[str, str, any], None] 
type Result = bool | Tuple[bool, str]

class Message(BaseModel):
    src: str
    topic: str
    data: Any

channels = {}
message_queue: List[Message] = []

MsgThread = {
    'flag': False,
    'delay': 0.1
}

def init():
    MsgThread['flag'] = True
    t = Thread(target = message_processor)
    t.start()

def exit():
    MsgThread['flag'] = False

def add_topic(src: str, topic_name: str):
    if src not in channels:
        channels[src] = {}
    
    channels[src][topic_name] = []

def subscribe_topic(src: str, topic_name: str, cb: MessageCB) -> Result:
    if (src not in channels) or (topic_name not in channels[src]):
        return False, 'Topic not published'
    else:
        channels[src][topic_name].append(cb)
        return True

def publish_message(src: str, topic_name: str, data: any):
    message_queue.append(Message(src = src, topic = topic_name, data = data))

def message_processor():
    """
    Thread function, process message and call all callbacks
    """
    while True:        
        if message_queue != []:
            msg = message_queue.pop(0)
            for callback in channels[msg.src][msg.topic]:
                try:
                    callback(msg.data)
                except:
                    ic('failed callback')
            # ic('processing')
            # ic(msg)
        elif MsgThread['flag'] == False:
            ic('quitting message processor thread')
            break
        time.sleep(MsgThread['delay'])
