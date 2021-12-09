#operator overloading
class A:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __add__(self, other):
        temp=A(0,0)
        temp.x=self.x+other.y
        temp.y=self.y+other.y
        return temp
    def __str__(self):
        return "p3 is addition"
    def __sub__(self, other):
        play=A(2,2)
        play.x=self.x-other.x
        play.y=self.y-other.y
        return play

    def show(self):
        print(self.x,self.y)
p1=A(10,30)
p2=A(60,80)
p3=p1+p2
print(p3)
p3.show()
p4=p1-p3
p4.show()