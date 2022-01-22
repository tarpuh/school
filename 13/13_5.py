class ReversedList:
    def __init__(self, L):
        self.spis = L[::-1]

    def __len__(self):
        return len(self.spis)

    def __getitem__(self, item):
        return self.spis[item]