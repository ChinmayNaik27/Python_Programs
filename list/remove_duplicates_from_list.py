"""Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""
list1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
temp=[]
for x in list1:
    for y in x:
        temp.append(y)
print(temp)
for x1 in temp:
    if x not in list2:

        i = temp.count(x1)
        if i != 1:
            temp.remove(x1)
print(temp)