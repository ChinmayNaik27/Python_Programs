#take a number from user and check the given number is amstrong number or not!!
try:
    s=int(input("Enter a number:"))
    s1=s
    sum=0
    while s>0:
        a=s%10
        s//=10
        sum+=a**3
    if s1==sum:
        print("Amstrog number!!")
    else:
        print("Not an amstong number!!")
except:
    print("Invalid input")