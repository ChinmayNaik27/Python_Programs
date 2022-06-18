#inner class or nested class
"""
class A:
    i=0
    def add1(self,a,b):
        self.a=a+a
        c=a+b
        return c
    class B:
        def add(self,a,b):
            c=a+b
            return c
    ob=B()
ob1=A()
x=ob1.add1(30,100)
print(x)
A=ob1.B()
c=ob1.ob.add(140,50)
print(c)"""
"""
class Student:
    def __init__(self):
        self.name='abc'
        self.age='23'

    def disp(self):
        print(self.name, self.age)
    class Dob:
        def __init__(self):
            self.dd=22
            self.mm=23
            self.yy=2013
        def disp(self):
            print(self.dd,self.mm,self.yy)
ob=Student()
ob.disp()
ob1=Student().Dob()                   #or ob1=ob.Dob()
ob1.disp()"""
#abstraction
"""
class Bank:
    def __init__(self):
        self.accno=1001
        self.phone = 123456789
        self.name = 'Abc'
        self.add = 'Aurangabad'
        self.bal = 56000.0
        self.__loan = 10000000.00
    def disp_to_clerk(self):
        print('accno={:d}'.format(self.accno))
        print('name={:s}'.format(self.name))
        print('address={:s}'.format(self.add))
        print('phone={:d}'.format(self.phone))
        print('Balence={:.2f}'.format(self.bal))

b=Bank()
b.disp_to_clerk()
print(b._Bank__loan)"""

from demo6 import *
#inheritance
class Teacher:
    def setId(self,id):             #setter menthord
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setAdd(self,add):
        self.add=add
    def getAdd(self):
        return self.add
    def setSal(self,Sal):
        self.Sal=Sal
    def getSal(self):
        return self.Sal