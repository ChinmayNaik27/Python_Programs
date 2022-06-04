"""Fixed Argument
def join(s1,s2):
    str=s1+s2
    print(str)

join('Auranga','bad') ##PA
join('bad','Auranga')"""
""" Keyword arguments:
def join(s1,s2):
    str=s1+s2
    print(str)

join(s1='Auranga',s2='bad') ##KWA
join(s2='Auranga',s1='bad')
join(s1='bad',s2='Auranga')"""
"""Default Arguments:
def gross(item,price=50.00):                                     # price is a default argument
    print(f"Item = {item}","Price={:.2f}".format(price),sep='\n')
gross('Sugar')
gross('Sugar',60)                          #changes value of sugar to 60
"""
"""variable length arguments or arbitary arguments:
def add(n,*x):
    total=n+sum(x)
    
    
    
    
    
    print(total)
add(10,10,12,23)
"""
"""recurssive function
def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res """

"""def decor(func):
    def inner():
        res=func()
        return res+10
    return inner
def myfunc():
    return 100

x=decor(myfunc)
print(x())"""

def ebill(units):
    if units<100:
        b=0
    elif units>=100 and units<500:
        b=units*10
    elif units>=500:
        b=units*15
    return b
units=float(input("Enter number of units Consumed:"))
a=ebill(units)
print(f"Total bill is :{a}")


def decor(fuc):
    def inner():
        res=fuc()
        res1=fuc()
        return res * res1
    return inner
@decor
def func():
    return 10
x=func()
print(x)