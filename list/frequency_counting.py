#WAP to count the frequency of each element in list
list1=[1,2,3,4,5,2,1,7,5,6,4,7,8,9,8,2,3,5,6]
temp=[]
for x in list1:
    i=list1.count(x)
    for x not in list1:
        print("Item Frequency of :",i,"is:",x)
        temp.append(x)