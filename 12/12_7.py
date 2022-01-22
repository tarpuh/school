class BoundingRectangle:
    def __init__(self):
        self.list_x = list()
        self.list_y = list()

    def add_point(self, x, y):
        self.list_x.append(x)
        self.list_y.append(y)

    def width(self):
        return max(self.list_x) - min(self.list_x)

    def height(self):
        return max(self.list_y) - min(self.list_y)

    def bottom_y(self):
        return min(self.list_y)

    def top_y(self):
        return max(self.list_y)

    def left_x(self):
        return min(self.list_x)

    def right_x(self):
        return max(self.list_x)
