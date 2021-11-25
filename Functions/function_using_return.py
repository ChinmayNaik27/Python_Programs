"""Functions using Return"""
#Defining functions
def div(x,y):
    """

    :param x: first number in x
    :param y: second no in y
    :return: division of x and y
    """
    d=x//y
    return d
#calling Function:
a=div(40,10)   #sets x=40,y=10
print(a)
print(div.__doc__)                                     #gives documentation of parametrs used in function