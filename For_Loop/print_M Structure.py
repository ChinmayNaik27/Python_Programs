"""WAP to print following structure
*     *
* * * *
*  *  *
*     *
*     *

"""
for i in range(5):
    for j in range(5):
        if j==0 or j==4 or (i==1 and (j==1 or j==3))  or (i==2 and j==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
