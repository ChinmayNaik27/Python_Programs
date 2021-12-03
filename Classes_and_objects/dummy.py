#calling_multiple_base_class:
class A:
    def __init__(self):
        print("In A")
        super().__init__()
class B:
    def __init__(self):

        print("In B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C")

ob=C()