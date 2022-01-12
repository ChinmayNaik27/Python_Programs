"""Remove Empty Tuples"""
list1=[(10,20),(30,40),(),(30,),(),(74,)]
for x in list1:
    print(len(x))
    if len(x)==0:
        list1.remove(x)
print(list1)
#2nd way
list2=[(10,20),(30,40),(),(),(30,),(),(74,)]
for x in list2:
    print(len(x))
    for y in list2:
        if len(y)==0:
            list2.remove(y)
print(list2)