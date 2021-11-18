#Write a program to calculate profit or loss.
a=float(input("Enter Cost Price:")) # take string input form user and convert to Float value
b=float(input("Enter Selling Price:"))  # take string input form user and convert to Float value
if (b-a)>0:                             #Profit=CP-SP
    print("Profit is:",b-a,"Rs")
elif (b-a)<0:                           #Loss=SP-CP
    print("Loss is",-(b-a),"Rs")
else:
    print("No Profit \nNo Loss")