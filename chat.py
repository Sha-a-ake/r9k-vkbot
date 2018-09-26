from user import User

class Chat():
    def __init__(self, sid):
        self.id = sid
        self.users = dict()
        self.words = dict()
        self.kicked = []

    def get_users(self, vk):
        for user_id in vk.messages.getChat(chat_id = self.id)['users']:
            self.users[str(user_id)] = User(user_id)

    def searchString(self, word):
        if not word in self.words:
            self.words[word] = True
            return False
        else:
            return True