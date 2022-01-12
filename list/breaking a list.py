"""Break a list into chunks of size N in Python"""
list1=[]
n=int(input("Enter total number of items to be entered inside a list:"))
for x in range(n):
    n=int(input("Enter item :"))
    list1.append(n)
print(list1)
n1=int(input("Enter a how many items you want  in a sublist:"))
temp=[]
for x1 in range(len(list1)):
    if x1<=n1:
        temp.append(list1[x1])
print(temp)
....