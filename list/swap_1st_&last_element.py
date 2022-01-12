"""program to interchange first and last elements in a list"""
list1=[10,20,30,40,50,60,40,10,20]
x=list1[-1]
list1[-1]=list1[0]
list1[0]=x
print(list1)