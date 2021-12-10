#SAMPLE PROGRAM PROJECTS
class Details:
    def __init__(self):
        self.id= "<No Id>"
        self.name= "<No Name>"
        self.gender= "<No Gender>"
    def setData(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
    def showData(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Gender: ", self.gender)

class Employee(Details): #Inheritance
    def __init__(self):
        self.company= "<No Company>"
        self.dept= "<No Dept>"
    def setEmployee(self,id,name,gender,comp,dept):
        self.setData(id,name,gender)
        self.company=comp
        self.dept=dept
    def showEmployee(self):
        self.showData()
        print("Company: ", self.company)
        print("Department: ", self.dept)

class Doctor(Details): #Inheritance
    def __init__(self):
        self.__hospital="<No Hospital>"
        self.__dept="<No Dept>"
    def setEmployee(self,id,name,gender,hos,dept):
        self.setData(id,name,gender)
        self.__hospital=hos
        self.__dept=dept
    def showEmployee(self):
        self.showData()
        print("Hospital: ", self.__hospital)
        print("Department: ", self.__dept)

def main():
    print("Employee Object")
    e=Employee()
    e.setEmployee(1,"Prem Sharma","Male","gmr","excavation")
    e.showEmployee()
    print("\nDoctor Object")
    d = Doctor()
    d.setEmployee(1, "pankaj", "male", "aiims", "eyes")
    d.showEmployee()

if __name__=="__main__":
    main()
