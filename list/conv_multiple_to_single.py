#WAP To Convert multiple integers to single integers
#Sample list=[11,33,22]
#output=11,33,22
a=int(input("Enter no of items in list:"))
list1=[]
s1=""
for x in range(a):
    q=input("Enter items:")
    list1.append(q)
for j in list1:
    s1=s1+j
s1=int(s1)
print(s1)