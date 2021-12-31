#WAP to concat a list which range goes from 0 to 10
#sample list=[p,q]
#sample output=['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']
list1=['p','q']
temp=[]
s1=""
n=int(input("Enter no of iterations:"))
for i in range(1,n+1):
    for j in list1:
        s1=j+str(i)
        temp.append(s1)
print(temp)
