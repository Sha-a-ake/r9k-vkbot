def friends_add(vk):
	friends = vk.friends.getRequests()
	for friend in friends['items']:
		vk.friends.add(user_id = friend, follow = 0)


def kick_user(vk, user, kicked):
    vk.messages.removeChatUser(chat_id = cid, user_id = user)
    kicked[str(event.user_id)] = time.time() + 10


def return_kicked(vk, kicked):
    t = time.time()
    for key, value in kicked.items():
        if t >= value:
            vk.messages.addChatUser(chat_id = cid, user_id = str(key))
            kicked.pop(key, None)
