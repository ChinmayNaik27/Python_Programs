class test():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    @classmethod
    def string(cls,msg):
        x,y,z=map(int,msg.split("-"))
        date=cls(x,y,z)
        return date
    @staticmethod
    def valid(msg):
        x,y,z=map(int,msg.split("-"))
        if x>=1 and x<=31 and y>=1 and y<=12:
            return True
        else:
            return False
    def show(self):
        print(self.x,self.y,self.z)
d1=test(10,2,2021)
d1.show()
d2=test.string("10-12-2021")
d2.show()
if d1.valid("4-12-2021"):
    print("Vaild")
else:
    print("Invaild")