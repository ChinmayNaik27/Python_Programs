"""WAP to take  a 3 digit number from user and check no is amstrong or not """
n=int(input("Enetr a 3 digit no:"))
n1=n
if n<999:
    b=n%10
    n//=10
    c=n%10
    n//=10
    d=n%10
    b=b*b*b
    c=c*c*c
    d=d*d*d
    sum=b+c+d
    if sum==n1:
        print("Its an Amrmstrong No")
    else:
        print("Not an Armstrong No")
else:
    print("No is more than 3 Digts.")