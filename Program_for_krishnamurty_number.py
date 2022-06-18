#program for krishnamurty number!!
def krish(x):
    i=1
    c=1
    while i<=x:
        c=c*i
        i+=1
    return c
s=int(input("Enter a number:"))
s1=s
sum=0
while s>0:
    a=s%10
    sum+=krish(a)
    s//=10
if s1==sum:
    print("It is a krishnamurty number!")
else:
    print("Not a krishnamurty number!!")
