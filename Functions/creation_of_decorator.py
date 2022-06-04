"""Creating a decorator for suqare values"""

def deco(fuc):
    def inner():
        res=fuc()
        return res * res
    return inner
def show1():
    x=int(input("Enter the value:"))
    return x
x=deco(show1)
print(x())
