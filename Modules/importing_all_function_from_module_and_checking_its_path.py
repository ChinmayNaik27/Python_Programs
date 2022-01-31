#importing all function from module and checking its path
from moduleimport import *   #importing all functions inside module
#Checking module paths
import sys
#using functions inside my module
x=add()
print(x)
y=sub(50,20)
print(y)
z=mul(10,50)
print(z)
w=intdiv(65,10)
print(w)
r=floatdiv(65,10)
print(r)
#printing paths where python checks for given module name
print(sys.path)
