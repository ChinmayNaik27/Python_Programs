#WAP Using Contructor
class Bulb:
    def __init__(self):                                                    #using inbulilt function or constructor
        self.company="Wipro"                                               #setting data
        self.power="230W"                                                 #setting data
        self.size="32B"                                                   #setting data
    def show(self):
        print("",self.company,"\n",self.power,"\n",self.size)

#calling function
b1=Bulb()
b1.show()