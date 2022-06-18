"""find factors of given number from user
eg: i/p=10
then o/p=[2,5]
i/p=12
op=[2,2,3] and so on.."""

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
