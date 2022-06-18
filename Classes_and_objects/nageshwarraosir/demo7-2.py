"""
s=int(input("Enter a number:"))
s1=s
sum=0
while s>0:
    a=s%10
    sum+=a**3
    s//=10
if sum==s1:
    print("Amstrong number!!")
else:
    print("Try again!!")
"""
"""def krish(x):
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
"""
"""
def gen1(x):
    i=0
    while i<=x:
        yield i
        i+=1
a=gen1(10)
for i in a:
    print(i)"""

"""
def chinmay(abc,x):
    def inner():
        r=abc(x)
        return r +10
    return inner
def abcqw(x):
    return x

a=chinmay(abcqw,20)
print(a)
print(a())
"""

"""s=int(input("Enter  a number:"))
i=2
if s==0 or s==1:
    print("Not a Prime number")
else:
    while i<s:
        if s%i==0:
            print("Not a Prime number!!")
            break
        i+=1
    if i==s:
        print("It is a Prime number!!")"""
"""s=int(input("Enter  a number:"))
first,second=0,1
for i in range(s):
        print(first)
        result=first+second
        first=second
        second=result
"""
while True:
    s=int(input("Enter a number:"))
    lst=[]
    while s > 1:
        if s % 2 == 0:
            lst.append(2)
        elif s % 3 == 0:
            lst.append(3)
        elif s % 5 == 0:
            lst.append(5)
        elif s % 5 == 0:
            lst.append(7)
        elif s % 5 == 0:
            lst.append(9)
        else:
            lst.append(s)
        s //= 2
    print(lst)
    n=input("Wish to continue??(yes/no):")
    n=n.lower()
    if n[0]=='n':
        break
