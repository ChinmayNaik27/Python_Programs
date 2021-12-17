"""WAP to print
    *
   **
  ***
 ****
*****"""
n=2
for i in range (6):
    k=0
    while k<n:
        print(" ",end=" ")
        n-=1
        k+=1
    for j in range(0,i):
        print("*",end="")

    print("")
