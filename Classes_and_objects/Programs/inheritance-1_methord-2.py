"""Create a class named ‘Animal’ which includes methods like eat() and sleep().
Create a child class of Animal named ‘Bird’ and override the parent class methods. Add a new method named fly().
Create an instance of Animal class and invoke the eat and sleep methods using this object.
Create an instance of Bird class and invoke the eat, sleep and fly methods using this object."""
class animal:
    def eat(self):
        print("This is eat Methord")
    def sleep(self):
        print("This is Sleep Function")
class Bird(animal):
    def eat(self):
        print("This is eat Methord in bird class")

    def sleep(self):
        print("This is Sleep Function in bird class")
    def fly(self):
        print("This is Fly Function")

ob1=animal()

ob2=Bird()
ob1.eat()
ob1.sleep()
ob2.eat()
ob2.sleep()
ob2.fly()