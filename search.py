
def init():
    words = dict()


def search(dic, word):
    if not word[0] in dic:
        dic[word[0]] = dict()
        if len(word) > 1:
            return search(dic[word[0]], word[1:])
    else:
        if len(word) > 1:
            return search(dic[word[0]], word[1:])
        else:
            print("found")
            return True


def searchf(word):
    return search(words, word)
