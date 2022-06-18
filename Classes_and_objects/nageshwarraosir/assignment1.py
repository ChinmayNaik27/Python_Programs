class Manager:
    def __init__(self,id,name,deptname,sal):
        self.id=id
        self.name=name
        self.dept=deptname
        self.sal=sal
    def salcalculation(self):
        self.ansal=self.sal*12
        if self.ansal<=250000:
            self.it=0
        else:
            self.it=self.ansal*0.10
        self.hra=self.ansal *0.155
    def show(self):
        print("Id is:",self.id)
        print("Name is:", self.name)
        print("Deptname is:", self.dept)
        print("Mothly Sal is:", self.sal)
        print("Annual sal is:",self.ansal)
        print("Income Tax is:", self.it)
        print("Hra is:", self.hra)
m1=Manager(12,'Ramesh','HR',200)
m1.salcalculation()
m1.show()
m2=Manager(13,'Ram','Technical',40000)
m2.salcalculation()
m2.show()
id=int(input("Enter Id:"))
name=input("Enter Name:")
dept=input("Enter Dept:")
sal=int(input("Enter Sal:"))
m3=Manager(id,name,dept,sal)
m3.salcalculation()
m3.show()