#WAP to count the frequency of each element in list
list1=[1,2,3,4,5,2,1,7,5,6,4,7,8,9,8,2,3,5,6]
temp=[]
for x in list1:
    if x not in temp:
        i=list1.count(x)
        print("Item Frequency of :",x,"is:",i)
        temp.append(x)
print(temp)