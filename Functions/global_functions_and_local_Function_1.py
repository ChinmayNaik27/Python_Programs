"""Program for local and global variable"""

#Defining local and global variable
#Global variable:
x=10
def show():
    #This is a local variable
    x=20
    print(x)

show()                        #output of local variable
print(x)                     #output of global variable