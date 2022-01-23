#without using filter function
def filter1(mylist11):
    temp=[]
    for x in mylist11:
        if x%2==0:
            temp.append(x)
    return temp
mylist=[1,2,3,4,5,6,7,8,9]
a=filter1(mylist)
print(a)