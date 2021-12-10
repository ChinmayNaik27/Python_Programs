#methord_overwriting
class A:                                                          #BASE CLASS
    def show(self):
        print("This is a ")
class B(A):
    def show(self):
        print("This is b")

ob=A()
ob.show()
ob1=B()
ob1.show()
