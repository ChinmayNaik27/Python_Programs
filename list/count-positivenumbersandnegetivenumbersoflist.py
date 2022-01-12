"""Program to count positive and negetive numbers in a list"""
list1=[10,20,30,40,-10,-20,-70,1,-2,-6,-9,-4,-10]
temp=[]
for x in list1:
    if x>0:
        temp.append(x)
print(temp)
print("Positive numbers are:",len(temp))
temp.clear()
for x in list1:
    if x<0:
        temp.append(x)
print(temp)
print("Negetive numbers are:",len(temp))