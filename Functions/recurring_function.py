"""createing a recurring function for fctorial"""

def fact(x):
    """
    this function is called untill x==0 in fact(x-1)
    """
    if x==0:
        res=1
    else:
        res=x*fact(x-1)
    return res
a=fact(5)
print(a)