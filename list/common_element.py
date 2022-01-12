"""Write a Python function that takes two lists and returns True if they have at least one common member"""
list1=[1,2,8,79,4,6,113,4,6]
list2=[1,2,3,4,5,6,78,9]
temp=[]
for x in list1:
    for y in list2:
        if x==y:
            temp.append(y)
if len(temp)>0 :
    print("List has common values\n",temp)
else:
    print("No Values")