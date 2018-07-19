
def init():
    global words
    words = dict()


def search(dic, word):
    if not word in dic:
        dic[word] = True
        return False

    return True


def searchf(word):
    return search(words, word)
