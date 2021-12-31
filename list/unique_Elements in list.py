list1=[1,2,3,4,2,7,55,6,9,7,9,5,1,4,3]
temp=[]
for x in list1:
    i=list1.count(x)
    if i==1:
        temp.append(x)
print(temp)
#2nd Way
list3=[1,2,3,5,3,8,6,2,4,5]
temp1=[]
for x1 in list3:
    i=0
    for z in list3:
        if x1==z:
            i=i+1
    if i==1:
        temp1.append(x1)
print(temp1)