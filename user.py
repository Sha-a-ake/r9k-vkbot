class User():
    def __init__(self, user_id):
        self.timeouts = 0
        self.isKicked = False
        self.isFriend = False
        self.id = user_id
