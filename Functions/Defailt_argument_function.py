"""Default argument function """
#Defining functions
def mod(x=20,y=10):
    """
    :param x: default value of x stored
    :param y: default value of y stored
    """
    mod=x%y
    print(mod)
#calling Function:
mod(40,10)   #sets x=40,y=10
mod(15)  #uses default value of y as 10 and set x =15
mod()   #uses default values