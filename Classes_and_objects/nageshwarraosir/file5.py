x=10
x1=30
def out1():
    global x1
    x=20
    y=globals()['x']
    print(type(y))
    print(x,y)
    print(x)
    print(x1)
    def out():
        print("Inner")
    return out()

out1()

