"""Write a program to implement a class “student” with the following members:
Name of the student. Marks of the student obtained in three subjects. Function to assign initial values.
 Function to compute total average. Function to display the student’s name and the total marks.
Write an appropriate main() function to demonstrate the functioning of the above."""
class student:
    def __init__(self):
        self.name=input("Enter name :")
        self.marks1=input("Enter marks of subject 1:")
        self.marks2 = input("Enter marks of subject 2:")
        self.marks3 = input("Enter marks of subject 3:")
    def avg(self):
        self.avg=(self.marks1+self.marks2+self.marks3)/3
        print("Average is:",self.avg)
    def show(self):
        print("Entered Data Is:\n","Name:", self.name,"Subject 1 marks:", self.marks1,"Subject 2 marks:", self.marks2,"Subject 3 marks:", self.marks3)

t1=student()
t1.show()
t1.avg()