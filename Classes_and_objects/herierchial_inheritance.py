#herarchial inheritance
class First:
    def __init__(self,x,y):
        self.x =x
        self.y = y


class Second(First):
    def __init__(self,p,q):
        super().__init__(p,q)
        self.z = self.x + self.y
        print("Sum is:", self.z)


class Third(First):
    def __init__(self,r,s):
        super().__init__(r,s)
        self.z = self.x - self.y
        print("Subtraction is:", self.z)

obj1 = Second(10,20)
obj2 = Third(20,40)