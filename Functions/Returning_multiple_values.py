#Program for returning Multiple Values
def flow(x,y):
    """
    :param x: first no
    :param y: second no
    :return: returns addition and substraction values
    """
    p=x+y
    q=x-y
    return p,q
a,b=flow(30,20)
print("Addition is:",a)
print("Substraction is:",b)
print(flow.__doc__)                              #printing documentation of function