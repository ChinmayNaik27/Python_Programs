"""class square:
    def __init__(self,l):
        self.len=l
    def area(self):
        self.area1=self.len*self.len
        print("Area of square:",self.area1)
class rectangle(square):
    def __init__(self,l,br):
        super().__init__(l)
        self.br=br
    def area(self):
        super().area()
        self.area=self.len * self.br
        print("Area of rectangle:",self.area)
a=int(input("Enter length :"))
b=int(input("Enter breath:"))
ob=rectangle(10,20)
ob.area()"""
#operator overloading -> same operator performing different classes
"""a=20
b=40
c=a+b                        # addiition
print(c)
a='Auranga'
b='Bad'
c=a+b                           #concatination
print(c)"""
#methord Overloading
"""class myclass():
    @staticmethod
    def add(*x):
        tot=sum(x)
        print("Sum=",tot)
myclass.add(10,11)
myclass.add(10,11,12)
myclass.add(10,11,13,12)
myclass.add(10,11,12,13,14)"""
#methord overwriting:
"""class A:
    def show(self):
        print("EHy")

class B:
    def show(self):
        print('Heyjbnkc')
s1=B()
s1.show()"""
#duck typing
"""
class Duck:
    def talk(self):
        print('Quack Quack!!')
class Dog:
    def talk(self):
        print('Bow wow!')
def call_talk(ob):
    ob.talk()

d=Dog()
call_talk(d)
d=Duck()
call_talk(d)"""