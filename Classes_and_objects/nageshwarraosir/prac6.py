class sqr:
    def square(self,sqr):
        self.sqr=sqr*sqr
class hyp(sqr):
    def __init__(self,sqr,sqr1):
        self.sqr1=sqr1*sqr1
        super().square(sqr)
        self.res=(self.sqr+self.sqr1) **0.5
    def show(self):
        print(f"Square of side 1 is:{self.sqr}",f"Square of side 2 is :{self.sqr1}",f"Third side by pythagoras therom is:{self.res}",sep='\n')
s1=int(input("Enter side 1:"))
s2=int(input("Enter side 2:"))
ob=hyp(s1,s2)
ob.show()