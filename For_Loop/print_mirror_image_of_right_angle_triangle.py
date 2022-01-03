"""WAP to print
    *
   **
  ***
 ****
*****"""
n=3
for i in range (1,5):
    k=0
    while k<n:
        print(" ",end="")
        k+=1
    n-=1
    for j in range(1,i+1):
        print("*",end="")
    print("")
