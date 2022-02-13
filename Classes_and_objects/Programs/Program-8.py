"""Write a class “Box” that with three member-variables “height”, “width” and “breadth”.
Write suitable constructors to initialize them.
Add functions like “getVolume” and “getArea” that will return volume and surface area respectively.
Create object of boxes and then print their volume and surface area."""
class Box:
    def dimenssions(self):
        self.length=float(input("Enter length:"))
        self.width=float(input("Enter Width:"))
        self.height=float(input("Enter Height:"))
    def getvolume(self):
        self.res=self.length*self.width*self.height
        print("Volume Is :",self.res)
    def getArea(self):
        self.res1=2*(self.length*self.width+self.length*self.height+self.width*self.height)
        print("Area is :",self.res1)
v1=Box()
v1.dimenssions()
v1.getvolume()
v1.getArea()