"""Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

list1=[1,2,3], [4,5,6], [10,11,12], [7,8,9]
list2=[]
for x in list1:
    a=sum(x)
    list2.append(a)
q=max(list2)
q1=list2.index(q)
for i in range(len(list1)):
    if i == q1:
        print(list1[i])

