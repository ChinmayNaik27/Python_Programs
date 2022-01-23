"""Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
list1=[{},{},{},{},{}]
a=True
b=False
temp=[]
for x in list1:
    for y in x:
        if len(x) != 0:
            temp.append(x)
if len(temp)==0:
    print(a)
else:
    print(b)
