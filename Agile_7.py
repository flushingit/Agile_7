class Word_P:
    def __int__(self):
        pass

    def reverse(self, word):
        return word[::-1]

    def seek_w(self, chars, word):
        char = [x for x in chars]
        if all(x in word for x in char):
            return chars
        else:
            return False