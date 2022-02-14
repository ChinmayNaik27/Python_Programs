"""Design a class ‘Complex ‘with data members for real and imaginary part.
Provide default and Parameterized constructors.
Write a program to perform arithmetic operations of two complex numbers."""
class Complex:
    def __init__(self,x,y):
        self.real=x
        self.img=y
    def __add__(self, other):
        temp=Complex(0,0)
        temp.real=self.real+other.real
        temp.img=self.img+other.img
        return temp
    def show(self):
        print(self.real,self.img)
t1=Complex(15,20)
t1.show()
t2=Complex(5,25)
t2.show()
t3=t1+t2
t3.show()