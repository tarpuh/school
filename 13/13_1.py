class LeftParagraph:
    def __init__(self, n):
        self.num = n
        self.l = ['']

    def add_word(self, word):
        if len(self.l[-1]) + len(word) > self.num:
            self.l.append(word + ' ')
        else:
            self.l[-1] += (word + ' ')

    def end(self):
        for elem in self.l:
            print(''.join(elem)[:-1])


class RightParagraph:
    def __init__(self, n):
        self.num = n
        self.l = ['']

    def add_word(self, word):
        if len(self.l[-1]) + len(word) > self.num:
            self.l.append(word + ' ')
        else:
            self.l[-1] += (word + ' ')

    def end(self):
        for elem in self.l:
            print((''.join(elem)[:-1]).rjust(self.num))