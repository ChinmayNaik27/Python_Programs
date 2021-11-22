# WAP to take a no. from user and print addition of its digit
n=int(input("Enter a number :"))    #input from user and convert it to int
i=1                                 #intialize i=1
while n>0:
    b=n%10
    n=n//10
    c=b+c
    i+=1
print(c)
