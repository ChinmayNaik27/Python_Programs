#Program for list Compression
list1=[1,2,3,12,4,5,6,2,2,55,9]
#without using if condition
list2=[x*x for x in list1]
print(list2)
#using if condition
list3=[x for x in list1 if x%2==0]
print(list3)