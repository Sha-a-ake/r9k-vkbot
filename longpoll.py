import search
import vk_functions

from vk_api.longpoll import VkLongPoll, VkEventType

def listen(longpoll, vk, chat_id, kicked):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.chat_id == chat_id:
            if search.duplicateString(event.text):
                vk_functions.kick_user(vk, event.user_id, kicked)
