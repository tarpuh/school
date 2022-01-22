class Rectangle:
    def __init__(self, x1, y1, w, h):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + w
        self.y2 = y1 + h
        self.list_of_x = list()
        self.list_of_y = list()

    def intersection(self, rect):
        self.list_of_x = sorted([self.x1, self.x2, rect.x1, rect.x2])
        self.list_of_y = sorted([self.y1, self.y2, rect.y1, rect.y2])
        if self.x1 >= rect.x2 or rect.x1 >= self.x2 or self.y1 >= rect.y2 or rect.y1 >= self.y2:
            return None
        else:
            return Rectangle(self.list_of_x[1], self.list_of_y[1], self.list_of_x[2] - self.list_of_x[1],
                             self.list_of_y[2] - self.list_of_y[1])

    def get_x(self):
        return self.x1

    def get_y(self):
        return self.y1

    def get_w(self):
        return self.x2 - self.x1

    def get_h(self):
        return self.y2 - self.y1