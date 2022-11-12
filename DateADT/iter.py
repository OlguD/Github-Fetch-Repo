class Bag():
    def __init__(self):
        self.a = list()

    def add(self, item):
        self.a.append(item)

    def __iter__(self):
        return BagIter(self.a)

    
class BagIter():
    def __init__(self, item):
        self.item = item
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 