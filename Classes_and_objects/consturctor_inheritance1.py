#basic Program for Constructor inhetitance
class A:
    def __init__(self):
        self.i=10
        print("In Class A")
class B(A):
    def __init__(self):
        super().__init__()
        self.j=20
        print("In Class B")
    def add(self):
        print(self.i+self.j)
ob1=B()
ob1.add()