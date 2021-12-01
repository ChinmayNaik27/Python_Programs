#Program to define instant methord
class test:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def show(self):
        print(self.id,self.name)
s1=test(1,"abc")
s2=test(2,"xyz")
s1.show()
s2.show()