#basic Program for Constructor inhetitance
class A:
    def __init__(self):
        self.i=10
        print("In Class A")
class B(A):
    def __init__(self):
        self.j=20
        super().__init__()                        #callin Value form class a
        print("In B")
    def add(self):
        print(self.i+self.j)
ob1=B()
ob1.add()