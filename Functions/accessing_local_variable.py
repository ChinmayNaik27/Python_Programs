"""using local Variable in nested function"""
#external Variable
from math import pi
#global Variable
pi=3.14

def outer():
    x=10
    print("This is Local Variable:",x)
    def inner():
        nonlocal x                #accessing value of outer function in inner function
        x=x+1
        print("This is value1:",x)
    inner()
    print(x)
print(pi)
outer()