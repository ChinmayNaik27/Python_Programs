#dummy
class First:
    def __init__(self):
        self.x = 20
        self.y = 10


class Second(First):
    def findsum(self):
        self.z = self.x + self.y
        print("Sum is:", self.z)


class Third(First):
    def findsub(self):
        self.z = self.x - self.y
        print("Subtraction is:", self.z)


obj1 = Second()
obj1.findsum()

obj2 = Third()
obj2.findsub()