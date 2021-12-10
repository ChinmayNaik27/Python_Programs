#WAP expection index error
print("Division of 2 nos:")
b=int(input("Enter index position:"))
list1=[10,20,60,30,4,15,60]
try:
    print(list1[b])
except IndexError as e2:
    print("Invaild Index")
print("End")