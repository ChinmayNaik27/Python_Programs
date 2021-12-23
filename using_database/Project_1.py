#importing module
from dbmodule import A
#Assigning Object
ob=A()
while True:
    x=int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update\nEnter no(Type any number to exit):"))
    if x==1:
        id = input("Enter id:")
        name = input("Enter name:")
        ob.insert(id,name)
    elif x==2:
        ob.select()
    elif x==3:
        id = input("Enter id:")
        ob.delete(id)
    elif x==4:
        id = input("Enter id:")
        name = input("Enter name:")
        ob.update(id,name)
    z=input("Enter y to continue and n to exit:")
    if z!='y':
        break
#closing Connection
ob.close()