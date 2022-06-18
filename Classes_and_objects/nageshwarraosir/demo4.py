"""
Types of varibable
"""
#instance variables
#accessor  methord and mutator methord
"""#code 1
class Employee:
    def __init__(self):
        self.name='Naru'
    #accessor methord or getter methord
    def getName(self):
        return self.name
    #muatator methord  or setter methord'
    def setName(self,name):
        self.name='laxmi'
ob=Employee()
a=ob.getName()                          #returning value is stored in a
print(a)
ob.setName('Sham')
str1=ob.getName()
print(str1)"""
# #code 2:
# class Employee:
#     """
#     Employee class for getter(accessor methord) and setter methord (Mutator Methord)
#     """
#     def __init__(self):
#         """
#         Setting values of name and sal
#         """
#         self.name='Shambhu'
#         self.sal=34500.67
#     #accessor methord or getter metords
#     def getName(self):
#         """
#         :return: return value of name
#         """
#         return self.name
#     def getSal(self):
#         """
#         :return: returns value of sal
#         """
#         return self.sal
#     #mutator methord or setter methord
#     def setName(self,name):
#         """
#         :param name:takes name as input
#         +:return: return modified name
#         """
#         self.name=name
#     def setsal(self):
#         """
#         :return: return upated sal
#         """
#         self.sal=500000.344
#
# ob1=Employee()
# a=ob1.getName()                     ########getter methord
# b=ob1.getSal()

# ob1.setsal()                          ########setter methord
# ob1.setName('Ramu')
# print(a)
# print(b)
# a1=ob1.getName()                       ########getter methord
# b1=ob1.getSal()
# print(a1)
# print(b1)
#class varibble and class methord
"""class Sample:
    #class Variable
    x=10
    #below is class methord
    @classmethod
    def modify(cls):
        cls.x+=10
s1=Sample()
s2=Sample()
print(s1.x,s2.x)
s1.modify()
print(s1.x,s2.x) 
s2.modify()
print(s1.x,s2.x)"""

#sattic vars and static methords
"""
class Sample:
    x=0
    def __init__(self):
        Sample.x+=1
    @staticmethod
    def display():
        print('No of objects are:',Sample.x)
s1=Sample()
s2=Sample()
s2=Sample()
Sample.display()"""

"""class Myclass:
    @staticmethod
    def sroot(x):
        x=x**0.5
        return x
ob=Myclass()
a=ob.sroot(25)
print(a)
res=Myclass.sroot(16 )
print(res)
"""