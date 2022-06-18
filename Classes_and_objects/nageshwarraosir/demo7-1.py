"""from demo7 import *
class Student(Teacher):
    def setmark(self,m1):
        self.marks=m1
    def getmarks(self):
        return self.marks

ob=Student()
ob.setid(123)
ob.setname('chamana')
ob.setqual('btech')
ob.setmark(340)
a=ob.getid()
b=ob.getname()
c=ob.getmarks()
print(a)
print(b)
print(c)"""
"""import functools as ft
class A:
    def add(self,a,b):
        c=a+b
        return c
    class B:
        def sub(self,*name):
            sub=ft.reduce(lambda x,y:x-y,name)
            return sub
    ob=B()

st=A().ob.sub(30,20,10)
print(st)"""

"""class A:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
         print(self.name)

ob=A('akshay',23)
ob.show()
print(ob._A__age)
"""

class fibonicii:
    @staticmethod
    def __init__(end):
        end=end ** 0.5
        print(end)
ob=fibonicii(50)
