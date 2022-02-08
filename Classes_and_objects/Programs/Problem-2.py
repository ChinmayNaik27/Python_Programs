"""Create a class that captures planets.
Each planet has a name, a distance from the sun, and its gravity relative to Earth’s gravity.
For distance and gravity, use the type double which captures real numbers.
Make objects for Earth and your favorite non-earth planet."""
class Planets:
    def __init__(self,pn,di,rg):
        self.pname=pn
        self.dist=di
        self.relgr=rg
    def show(self):
        print("Your Entered Data is :","\nPlanet Name:", self.pname,"\nRelative Gravity:", self.relgr,"\nDistance(in km):", self.dist)

p1=Planets('Earth',6586547414.5,'9.8')
p2=Planets('Venus',865957163.8,'6.58')
p1.show()
p2.show()