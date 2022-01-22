class BigBell():
    def __init__(self):
        self.a = 0

    def sound(self):
        if self.a % 2 == 0:
            print('ding', end='')
        else:
            print('dong', end='')
        self.a += 1