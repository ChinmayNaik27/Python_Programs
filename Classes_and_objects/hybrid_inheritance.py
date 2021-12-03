class student:
    def setdata(self):
        self.name=input("Enter Your Name:")
        self.id=int(input("Enter id: "))
    def showdata(self):
        print(self.name,self.id)
class marks(student):
    def setmarks(self):
        self.m1=int(input("Enter Your Marks1:"))
        self.m2=int(input("Enter Enter your Marks2:"))
    def showmark(self):
        print(self.m1,self.m2)
class sport:
    def nameandgrade(self):
        self.name1=input("Enter Your Sport:")
        self.grade=int(input("Enter marks: "))
    def gmark(self):
        print(self.name1,self.grade)
class result(marks,sport):
    def result(self):
        self.setdata()
        self.setmarks()
        self.nameandgrade()
    def display(self):
        self.showdata()
        self.showmark()
        self.gmark()
        avg=(self.m1+self.m2+self.grade)/2
        print("Average Value:",avg)
ob=result()
ob.result()
ob.display()