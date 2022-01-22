class Queue:
    def __init__(self, *que):
        self.que = list()
        for elem in que:
            self.que.append(str(elem))

    def append(self, *values):
        for elem in values:
            self.que.append(str(elem))

    def copy(self):
        return Queue(*self.que)

    def pop(self):
        return self.que.pop(0)

    def extend(self, que_2):
        for elem in que_2.que:
            self.que.append(str(elem))

    def next(self):
        return Queue(*self.que[1::])

    def __add__(self, other):
        a = self.que[::]
        for elem in other.que:
            a.append(str(elem))
        return Queue(*a)

    def __iadd__(self, other):
        for elem in other.que:
            self.que.append(str(elem))
        return Queue(*self.que)

    def __eq__(self, other):
        return self.que == other.que

    def __rshift__(self, n):
        if n <= len(self.que):
            return Queue(*self.que[n::])
        else:
            return None

    def __str__(self):
        a = '[' + '->'.join(self.que) + ']'
        return a

    def __next__(self):
        return Queue(*self.que[1::])