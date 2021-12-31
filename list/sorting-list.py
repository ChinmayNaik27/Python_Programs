# #WAP to sort a list taken from user
list1=[]
a=int(input("Enter items of in list:"))
i=0
while i<a:
    x=input("Enter element:")
    list1.append(x)
    i+=1
print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)

