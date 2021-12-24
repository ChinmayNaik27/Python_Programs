#WAP to select even numbers from a list
list1=[1,2,3,4,5,6,9,8,7,10]
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
print(list2)