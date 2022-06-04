def gen1(m,n):
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