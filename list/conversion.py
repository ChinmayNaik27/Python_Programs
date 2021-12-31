#WAP to convert given value into binary
list1=[]
a=int(input("Enter a number:"))
z=a
while a>0:
    x=a%2
    a//=2
    list1.append(x)
list1.reverse()
print("Binary for given no:",z," is:",list1)