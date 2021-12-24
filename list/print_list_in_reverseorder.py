#WAP to print list in reverse order without using reverse function
list1=[1,2,3,4,5,6,9,8,0,7]
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end=" ")
