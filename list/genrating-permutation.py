"""Write a Python program to generate all permutations of a list in Python"""
list1=[1,2,3,4,5,6,7,8,9,10]
temp=[]
for i in range(len(list1)):
    for j in range(len(list1)):
        temp.append(str(list1[i])+str(list1[j]))
print(temp)