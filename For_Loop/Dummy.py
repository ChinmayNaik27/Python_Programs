"""WAP to Print Following Structure
* * * * *
       *
     *
   *
* * * * *
"""
a=0
b=0
for a in range(5):
    for b in range(5):
        if a == 0 or a == 4 :
            print("*",end=" ")
        elif (a==2 and b==2) or (a==1 and b==3) or (a==3 and b==1):
            print("*",end="")
        else:
            print(" ", end=" ")
    print()