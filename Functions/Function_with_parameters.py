"""WAP for a function with fixed parameters"""
#defining a function
def mul(x,y):
    """
    :param x: first number
    :param y: second number
    """
    mul=x*y
    print(mul)
def area(r):
    """
    :param r: radius of circle
    """
    a=3.14*r*r
    print("Area Of Circle:",a)
#calling a function
mul(10,5)
area(1.2)
print(area.__doc__)                             #specifies parametrs of area function
print(mul.__doc__)                               #specifies parametrs of mul function