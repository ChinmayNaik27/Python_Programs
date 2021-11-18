# Progarm to Swap the contents of 2 no's
a=int(input("Enter no1:"))             #take input form user in integer format
b=int(input("Enter no2:"))             #take input form user in integer format
c=0                                    #Set c=0
print("Input Nos. are \t No1 :",a,b)
c=a                                    # value of A assigned to c
a=b                                    # value of B assigned to a
b=c                                    # value of C assigned to b
print("Execution Results:\t",a,b)