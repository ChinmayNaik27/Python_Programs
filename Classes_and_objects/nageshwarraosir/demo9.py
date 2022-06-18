"""#abstract class and abstract methord!!
from abc import ABC,abstractmethod
class Myclass(ABC):
    def disp(self):
        print("Hey this is concrete methord!!!")
    @abstractmethod
    def cal(self,x):
        pass
class sub1(Myclass):
    def cal(self, x):
        print("Square is :",x*x)
import math
class sub2(Myclass):
    def cal(self, x):
        print("Square root is : ",math.sqrt(x))
s1=sub1()
s1.disp()
s1.cal(16)
s2=sub2()
s2.disp()
s2.cal(16)
"""
#an inteface to connect to any db in the world
"""from abc import *
class myint(ABC):
    @abstractmethod
    def connect(self):
        pass
class oracle(myint):
    def connect(self):
        print("Connect to oracle!!")
class sybase(myint):
    def connect(self):
        print("Connecting to sydba!!")

str=input("Enter your database:")
classname=globals()[str]
c=classname()
c.connect()"""
"""import time
ep=time.time()
print(ep)
dt=time.ctime(ep)
print(dt)"""
"""from datetime import *
d,m,y=[int(i) for i in input().split('/')]
dt=date(y,m,d)
str=dt.strftime("You were born on %A and it is %jth day in the year.")
print(str)"""

"""from datetime import *
dt=datetime(2022,6,16,10,4,30)
dur=timedelta(weeks=3,days=10,hours=10,minutes=23)
print(dt+dur)
print(dt-dur)
"""