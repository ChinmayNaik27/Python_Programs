"""Python practice oopss!!"""
#classes and objects
class Person:
    def __init__(self):
        self.name='Chinmay'
        self.age=23
    def talk(self):
        print("Hello",self.name)
        print("Your age is",self.age)
class Person1:
    def __init__(self,name='Hey',age=0):
        self.name=name
        self.age=age
    def talk(self):
        print("Hello",self.name)
        print("Your age is",self.age)
class Student:                                                              #with parameters
    def __init__(self,rno,name,add,*nam):                        # if instead of *nam we use nam follow comment
        self.rno=rno
        self.name=name
        self.address=add
        self.lst=nam                              #if *name is given as name then self.lst=[int(i) from i nam.split(",")] or pass list inside parameter
        self.x1=(sum(self.lst)*100)/500
    def result(self):
        print("Name is:",self.name)
        print("RollNo is:", self.rno)
        print("Address is:", self.address)
        print("Percentage is:", self.x1,"%")
class Student1:                                                        #zero parametrs or default parametrs!!
    def __init__(self):
        self.rno=21
        self.name='Jaga Daku'
        self.address='Patna Ka Pahadi elaka'
        self.lst=[67,78,56,67,59]
        self.lst=sum(self.lst *100)/500
    def result1(self):
        print("Name is:",self.name)
        print("RollNo is:", self.rno)
        print("Address is:", self.address)
        print("Percentage is:{:.2f}%".format(self.lst))

ob=Person()
ob.talk()
print(ob)
ob1=Person1()
ob1.talk()
S1=Student(10,'abc','Near Gevrai Tanda,Aurangabad',100,99,65,78,100)
S1.result()
S2=Student1()
S2.result1()
rno=int(input("Enter rno:"))
name=input("Enter name:")
address=input("Enter address:")
                                       #marks=[int(i) for i in input("Enter your marks").split(',')]
S3=Student(rno,name,address,marks)
S3.result()