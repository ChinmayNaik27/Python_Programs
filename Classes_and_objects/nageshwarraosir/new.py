n=5
# n=int(input("Enter number of rows:"))
a=1
b=n-1

for i in range(n):
    for j in range(n):
        if (i==1 and j%2==0) or (i==3 and j%2 !=0) or (i==0 and j%2 !=0) or (i==4 and j==2) or (i==2 and (j==0 or j==4)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
