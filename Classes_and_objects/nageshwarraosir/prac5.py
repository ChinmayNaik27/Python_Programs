class A:
    def __init__(self,id):
        self.id=id
    def disp(self):
        print(self.id)
class B(A):
    def __init__(self,id,name):
        super().__init__(id)
        super().disp()
        self.name=name
    def disp(self):
        print(self.id,self.name)
ob=B(12,'xyz')
ob.disp()