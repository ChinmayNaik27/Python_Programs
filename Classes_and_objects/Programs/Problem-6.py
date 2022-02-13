"""Create a class “Room” which will hold the “height”, “width” and “breadth” of the room in three fields(variables).
This class also has a method “volume()” to calculate the volume of this room."""
class Room:
    def dimenssions(self):
        self.length=float(input("Enter length:"))
        self.width=float(input("Enter Width:"))
        self.height=float(input("Enter Height:"))
    def volume(self):
        self.res=self.length*self.width*self.height
        print("Volume Is :",self.res)
v1=Room()
v1.dimenssions()
v1.volume()