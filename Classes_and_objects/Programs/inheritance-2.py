"""Create a class called Person with a member variable name.
Save it in a file called Person.java Create a class called Employee who will inherit the Person class.
The other data members of the employee class are annual salary (double),
the year the employee started to work, and the national insurance number which is a String.
Save this in a file called Employee.java Your class should have a reasonable number of constructors and accessor methods.
 Write another class called TestEmployee, containing a main method to fully test your class definition"""
class Person:
    def anualsalary(self):
        self.sal = int(input("Enter the anual salary:"))
        self.sal*=2

    def workingyear(self):
        self.yr = int(input("Enter Your Staring Year of Work:"))

    def nationalic(self):
        self.id = input("Enter Your National Insurance Number:")
class Employee(Person):
    def methord1(self):
        self.anualsalary()
        self.workingyear()
        self.nationalic()
    def show(self):
        print("Entered Details Are:\n","Working Year:",self.yr,"\nAnual Salary(double):",self.sal,"\nNational Insurance Number:",self.id)
ob1=Employee()
ob1.methord1()
ob1.show()
