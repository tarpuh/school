class MinMaxWordFinder:
    def __init__(self):
        self.max_lenth = 0
        self.min_lenth = 0
        self.max_words = list()
        self.min_words = list()

    def add_sentence(self, sentence):
        for word in list(map(str, sentence.split())):
            if self.min_lenth == 0:
                self.min_lenth = len(word)
                self.min_words.append(word)
            elif len(word) == self.min_lenth:
                self.min_words.append(word)
            if len(word) > self.max_lenth:
                self.max_lenth = len(word)
                self.max_words = list()
                self.max_words.append(word)
            if len(word) == self.max_lenth and word not in self.max_words:
                self.max_words.append(word)
            if len(word) < self.min_lenth:
                self.min_lenth = len(word)
                self.min_words = list()
                self.min_words.append(word)

    def longest_words(self):
        return sorted(self.max_words)

    def shortest_words(self):
        return sorted(self.min_words)