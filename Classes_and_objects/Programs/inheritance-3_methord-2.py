"""A HighSchool application has two classes: the Person superclass and the Student subclass.
Using inheritance, in this lab you will create two new classes, Teacher and CollegeStudent.
A Teacher will be like Person but will have additional properties such as salary (the amount the teacher earns) ,
and subject (e.g. “Computer Science”, “Chemistry”, “English”, “Other”).
The CollegeStudent class will extend the Student class by adding a year (current level in college)
and major (e.g. “Electrical Engineering”, “Communications”, “Undeclared”)."""

class Person:
    def __init__(self):
        self.name = input("Enter Your Name :")
        self.id=int(input("Enter College PRN:"))
class Student(Person):
    def __init__(self):
        super().__init__()
class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.salary=int(input("Enter Your Salary:"))
        self.tsubject=input("Enter Your Subject:")
    def show(self):
        print("Teacher's name:",self.name,"\nTeachers Id is :",self.id,"\nThe Salary Of Techer is:",self.salary,"\nThis is Your Teaching Subject:",self.tsubject)

class collegestudent(Student):
    def __init__(self):
        super().__init__()
        self.year=input("Enter Your Year:")
        self.major=input("Enter Your Stream\Field:")
    def display(self):
        print("Student's name:", self.name, "\nStudents Id is :", self.id,
              "\nYour Year is:", self.year, "\nYour Stream is:", self.major)

ob1=Teacher()
ob2=collegestudent()
ob1.show()
ob2.display()