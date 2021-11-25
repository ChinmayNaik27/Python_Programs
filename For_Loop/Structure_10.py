"""WAP to Print Following Structure
*
*
*
*
* * * * *
"""
a=0
b=0
for a in range(5):
    for b in range(5):
        if a == 4 or b == 0 :
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()