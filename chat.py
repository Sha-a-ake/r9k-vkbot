from user import User

class Chat():
    def __init__(self, sid):
        self.id = sid
        self.users = dict()
        self.words = []
        self.kicked = []

    def get_users(self, vk):
        for user_id in vk.messages.getChat(chat_id = self.id)['users']:
            self.users[str(user_id)] = User(user_id)
