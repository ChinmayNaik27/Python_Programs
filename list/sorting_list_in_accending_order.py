#WAP to get a list ,sorted in increasing order by the last element in each list from given list of non-empty list
"""
sample list=[[2,5],[1,2,5],[4,4],[2,3],[2,1]]
output=[[2,1],[2,3],[4,4],[1,2,5],[2,5]]
"""
mylist=[[2,5],[1,2,5],[4,4],[2,3],[2,1]]
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[j][-1]>mylist[j+1][-1]:
            x=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=x
print(mylist)