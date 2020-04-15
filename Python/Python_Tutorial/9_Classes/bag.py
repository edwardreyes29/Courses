# methods may call other methods by using attributes of self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

b = Bag()

b.addtwice(4)
print(b.data)