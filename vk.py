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

def kick_user(vk, user):
    vk.messages.removeChatUser(chat_id = cid, user_id = user)
    kicked[str(event.user_id)] = time.time() + 10


def return_kicked(vk):
    t = time.time()
    for key, value in kicked.items():
        if t >= value:
            vk.messages.addChatUser(chat_id = cid, user_id = str(key))
            kicked.pop(key, None)


def longpoll_listen(longpoll, vk):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.chat_id == cid:
            if search.duplicateString(event.text):
                kick_user(vk, event.user_id)

        return_kicked(vk)


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
    friends_add(vk)

'''    while True:
        print("Listening")
        try:
            longpoll_listen(longpoll, vk)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as error:
            print(error)'''


def friends_add(vk):
	friends = vk.friends.getRequests()
	for friend in friends['items']:
		vk.friends.add(user_id = friend, follow = 0)


if __name__ == '__main__':
    search.init()
    main() 
