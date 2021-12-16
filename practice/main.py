from abc import ABC,abstractmethod
class A(ABC):
    def show(self):
        print("In CLass A ")
    @abstractmethod
    def add(self,x,y):
        pass
class B(A):
    def disp(self):
        print("In B")

    def add(self, x, y):
        print(x+y)
ob=B()
ob.show()
ob.disp()
ob.add(10,60)