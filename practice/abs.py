class Human:
    def talk(self):
        print("Hey")
class Duck:
    def talk(self):
        print("quack quack")
class Dog:
    def bark(self):
        print("Bho Bho")
def show(ob):
    if hasattr(ob,'talk'):
        ob.talk()
    else:
        ob.bark()
t1=Human()
t2=Duck()
t3=Dog()
show(t1)
show(t2)
show(t3)