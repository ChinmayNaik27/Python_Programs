from abc import ABC,abstractmethod

class A(ABC):
    def show(self):
        print("this is class A")
    @abstractmethod
    def add(self,x,y):
        pass

class B(A):
    def display(self):
        print("This is class B")

    def add(self, x, y):
        print(x+y)
        print(x*y)
ob=B()
ob.show()
ob.display()
ob.add(20,30)