class Button():
    def __init__(self):
        self.cliks = 0

    def click(self):
        self.cliks += 1

    def reset(self):
        self.cliks = 0

    def click_count(self):
        return self.cliks