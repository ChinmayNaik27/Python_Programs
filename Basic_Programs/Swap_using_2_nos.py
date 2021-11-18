""" Write Swap Progarm Using 2 Variables only"""
print("Progarm Using 2 Variables only")
a=int(input("Enter no1:"))                         #take input form user in integer format
b=int(input("Enter no2:"))                          #take input form user in integer format
print("Input Nos. are \t No1 :",a,b)
a=a+b                                               #Add values of a and b and store in a
b=a-b                                               #Substract Values of a and b store in b
a=a-b                                               #Substract values of aand b store in a
print("Execution Results:\t",a,b)