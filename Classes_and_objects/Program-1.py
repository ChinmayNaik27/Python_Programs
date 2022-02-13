"""check object has equal parameter or not"""
class Point:
    def __init__(self,x,y):
        self.i=x
        self.j=y
    def __eq__(self, other):
        if self.i==other.i  and self.j==other.j:
            return True
        else:
            return False
    def show(self):
        print(self.i,self.j)
p1=Point(10,20)
p2=Point(10,30)
if p1==p2:
    print("Both Values Are same")
else:
    print("Values Different")