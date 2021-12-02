#Program For Simple Inheritance
class student:
    def setdata(self):
        self.name=input("Enter Your Name:")
        self.id = int(input("Enter Your Id:"))
    def showdata(self):
        print(self.id,self.name)
class marks(student):
    def setmarks(self):
        self.marks1=int(input("Enter  marks for 1st subject:"))
        self.marks2 = int(input("Enter  marks for 2nd subject:"))
    def showmarks(self):
        print(self.marks1,self.marks2)
ob1=marks()
ob1.setdata()
ob1.setmarks()
ob1.showdata()
ob1.showmarks()
