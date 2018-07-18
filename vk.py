import random
import time
import sys
import getpass

import search

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

kicked = dict()

# conference id
cid = 84


def longpoll_listen(longpoll, vk_session):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.chat_id == cid:
            if search.searchf(event.text):
                vk_session.messages.removeChatUser(chat_id = cid, user_id = event.user_id)
                kicked[str(event.user_id)] = time.time() + 10
        t = time.time()
        print(kicked)
        for key, value in kicked.items():
            if t > value:
                vk_session.messages.addChatUser(chat_id = cid, user_id = str(key))
                kicked.pop(key, None)


def main():
    not_authed = True
    vk_session = vk_api.VkApi(input('Аккаунт: '), getpass.getpass('Пароль: '))

    while not_authed:
        try:
            vk_session.auth()
            not_authed = False
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

    print("Login successful")

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    while True:
        print("Listening")
        try:
            longpoll_listen(longpoll, vk)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as error:
            print(error)
 

if __name__ == '__main__':
    search.init()
    main() 
