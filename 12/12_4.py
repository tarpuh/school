class OddEvenSeparator():
    def __init__(self):
        self.list_odd = list()
        self.list_even = list()

    def add_number(self, number):
        if number % 2 == 0:
            self.list_even.append(number)
        else:
            self.list_odd.append(number)

    def even(self):
        return self.list_even

    def odd(self):
        return self.list_odd
