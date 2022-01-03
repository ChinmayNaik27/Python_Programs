#WAP to count the frequency of each item present in the list & display it in dict format
mylist=[1,2,3,2,3,3,7,5,1,8,1,1,2]
d1=dict()                 #empty dictionary
for x in mylist:
    p=0
    for y in mylist:
        if x==y:
            p=p+1
        d1[x]=p
print(d1)