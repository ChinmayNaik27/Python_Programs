"""def gen1(m,n):
    while m<=n:
        yield m
        m+=1
def function1():
    return "Hello"
def myfunc(abc):
    r=abc()
    return r + "Hello"
def func(abc):
    return abc()+' ' +"Krish"
a=gen1(30,40)

for i in a:
    print(i,end=' ')
a=function1()
print(a)
a=myfunc(function1)
print(a)
a=func(function1)
print(a)

def deco(func):
    def ageing():
        res=func()
        return res*res
    return ageing
def samp():
    x=int(input("Enter input:"))
    return x

x=deco(samp)
print(x())
"""
a=bytes([10,20,33,45,6,77,255])
type(a)
print(a[0])
b=bytearray([10,22,34,5,66,56,78])
print(b)
b[0]=20
for i in a:
    print(i,end='')
for i1 in b:
    print(i1,end=' ')
print()
x=int(input("Enter no:"))
print(x)
print(bin(x))
print(hex(x))
print(oct(x))