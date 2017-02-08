class Heap():
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)
        self.shift_up(len(self.array)) # len(array) is new index

    def shift_up(self, index):
        pass

    def pop(self):
        value = self.array[0]
        self.array[0] = None
        self.collapse(0)
        return value

    def peek(self):
        return self.array[0]

    def collapse(self, index):
        pass
