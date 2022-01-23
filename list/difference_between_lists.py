"""Write a Python program to get the difference between the two lists."""
list1=[1,2,3,4,5,6,7]
list2=[7,8,9,4,0,2,3]
list3=[]
for x in list1:
    for y in list2:
        list3.append(abs(x-y))
print(list3)