#WAP to conv Flatten list to shallow list
"""
oriinal list=[[2,4,3],[1,5,6],[9],[7,9,0]]
output[2,4,3,1,5,6,9,7,9,0]
"""
list1=[[2,4,3],[1,5,6],[9],[7,9,0]]
temp=[]
for list2 in list1:
    for j in list2:
        temp.append(j)
print(temp)