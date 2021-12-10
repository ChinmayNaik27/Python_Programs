#WAP expection zerodivision error
print("Division of 2 nos:")
a=int(input("Enter no1 :"))
b=int(input("Enter no 2:"))

try:
    c=a/b
    print("Div is c:",c)
except ZeroDivisionError as e1:
    print("infinity")
print("End")