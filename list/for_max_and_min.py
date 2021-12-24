#WAP for max and min
list1=[10,2,3,7,9,20,56,0,7,4692,697]
x=list1[0]
x1=list1[0]
for i in list1:
    if i>x:
        x=i
print("Max no is :",x)
for j in list1:
    if j<x1:
        x1=j
print("Min no is :",x1)
#2nd way using inbuilt functions
print(min(list1))
print(max(list1))