class SeaMap:
    def __init__(self):
        self.ground = list()
        for i in range(10):
            self.ground.append(list('..........'))

    def cell(self, x, y):
        return self.ground[x][y]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.ground[row][col] = '*'
        if result == 'hit':
            self.ground[row][col] = 'X'
        if result == 'sink':
            self.ground[row][col] = 'X'
            SeaMap.sink_procces(self, row, col, 11, 11)

    def sink_procces(self, row, col, exeption_row, exeption_col):
        new_row = row - 1
        new_col = col - 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_row = row
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col - 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_row = row + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)

    def cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col):
        if (new_row != exeption_row or new_col != exeption_col) and -1 < new_row < 10 and -1 < new_col < 10:
            if self.ground[new_row][new_col] == 'X':
                SeaMap.sink_procces(self, new_row, new_col, row, col)
            else:
                self.ground[new_row][new_col] = '*'