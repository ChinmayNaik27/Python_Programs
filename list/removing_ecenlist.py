#WAP to remove even items from list
lis1=[1,2,3,4,5,6,7,8,9,10]
for x in lis1:
    if x%2==0:
        lis1.remove(x)
print(lis1)