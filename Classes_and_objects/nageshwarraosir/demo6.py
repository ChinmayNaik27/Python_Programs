from demo5 import *
class Student(Teacher):
    def setMarks(self,marks):
        self.marks=marks
    def getAMarks(self):
        return self.marks

ob=Student()
ob.setName('Ramu')
ob.setId(123)
ob.setAdd('Aurangabad')
ob.setMarks(300)
print(ob.getName())
print(ob.getId())
print(ob.getAdd())
print(ob.getAMarks())