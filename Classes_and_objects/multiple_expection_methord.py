#WAP multiple expection
print("Division of 2 nos:")
a=int(input("Enter no1 :"))
b=int(input("Enter no 2:"))
list1=[10,20]
try:
    print(list1[b])
    c=a/b
    print("Divion is :",c)
except ZeroDivisionError as e1:
    print("Infinity")
except IndexError as e2:
    print("invaild index")
print("End")