#program for multi-level inheritance
class student:
    def setdata(self):
        self.name=input("Enter Your Name:")
        self.id = int(input("Enter Your Id:"))
    def showdata(self):
        print(self.id,self.name)
class marks:
    def setmarks(self):
        self.m1=int(input("Enter  marks for 1st subject:"))
        self.m2 = int(input("Enter  marks for 2nd subject:"))
    def showmarks(self):
        print(self.m1,self.m2)
class result(student,marks):
    def setresult(self):
        self.setdata()
        self.setmarks()

    def showresult(self):
        self.showdata()
        avg=(self.m1+self.m2)/2
        self.showmarks()
        print("Average result is :",avg)
ob1=result()
ob1.setresult()
ob1.showresult()