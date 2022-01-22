class Table:
    def __init__(self, row, col):
        self.rows = row
        self.col = col
        self.tab = list()
        for _ in range(row):
            self.row = list()
            for _ in range(col):
                self.row.append(0)
            self.tab.append(self.row)

    def get_value(self, row, col):
        if 0 <= row < len(self.tab) and 0 <= col < len(self.tab[0]):
            return self.tab[row][col]
        else:
            return None

    def set_value(self, row, col, amount):
        self.tab[row][col] = amount

    def n_rows(self):
        return len(self.tab)

    def n_cols(self):
        return len(self.tab[0])

    def delete_row(self, n):
        self.tab.pop(n)

    def delete_col(self, n):
        for elem in self.tab:
            elem.pop(n)

    def add_row(self, n):
        self.row = list()
        for _ in range(self.col):
            self.row.append(0)
        x = self.tab[:n]
        x.append(self.row)
        x += self.tab[n:]
        self.tab = x

    def add_col(self, n):
        for i in range(len(self.tab)):
            x = self.tab[i][:n]
            x.append(0)
            x += self.tab[i][n:]
            self.tab[i] = x
