#WAP using lambda as a function
# printing square using lambda function
x=lambda a:a*a
print(x(10))
#using filter and map function in lambda
list1=[1,2,3,4,5,6,7,8,9,10]
list2=filter(lambda x:x%2,list1)
print(list2)                                         #gives you the output of filter object
list2=list(filter(lambda x:x%2,list1))               #converts the output into list format
print(list2)
list3=map(lambda x:x*x,list1)                        #gives you the output of map object
print(list3)
list3=list(map(lambda x:x*x,list1))                   #converts the output into list format
print(list3)