class a():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        temp=a(0,0)
        temp.x=self.x+other.x
        temp.y=self.y+ other.y
        return  temp
    def __str__(self):
        return "Wait"
    def show(self):
        print(self.x,self.y)
t1=a(10,20)
t1.show()
t2=a(160,70)
t2.show()
t3=t1+t2
t3.show()
print(dir(t1))
print(t1)
print(t2)