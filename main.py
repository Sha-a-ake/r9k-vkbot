import random
import time
import sys
import getpass

import search
import vk_functions
import longpoll

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

kicked = dict()

# conference id
cid = 84

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

    while True:
        print("Listening")
        try:
            longpoll.listen(longpoll, vk)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as error:
            print(error)


if __name__ == '__main__':
    search.init()
    main() 
