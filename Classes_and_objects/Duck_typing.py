#duck typing
class A:
    def show(self):
        print("Hey Buddy")
class B:
    def show(self):
        print("Quack Quack")
class C:
    def dis(self):
        print("Haahaa")

def dodo(ob):
    if hasattr(ob,'show'):        #CHECKING FOR FUCTION
        ob.show()
    else:
        ob.dis()
t=A()
z=B()
q=C()
dodo(t)
dodo(q)
dodo(z)
