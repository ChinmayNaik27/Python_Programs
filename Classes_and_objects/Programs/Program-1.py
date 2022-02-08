"""Create a class that captures students. Each student has a first name, last name, class year, and major.
Create two examples of students."""
class student:
    def __init__(self,fn,ln,yr,mj):
        self.first=fn
        self.last=ln
        self.year=yr
        self.major=mj

    def show(self):
        print("Your Entered Data is :\n",self.first,self.last,self.year,self.major)

s1=student('Raju','Mishra','F.E','CSE')
s2=student('Kamal','Ratul','T.E','E&tc')
s1.show()
s2.show()