class Balance():
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, x):
        self.right += x

    def add_left(self, y):
        self.left += y

    def result(self):
        if self.right > self.left:
            return 'R'
        elif self.right < self.left:
            return 'L'
        else:
            return '='