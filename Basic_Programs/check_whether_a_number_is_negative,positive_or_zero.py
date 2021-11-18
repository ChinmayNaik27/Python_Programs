#program to check whether a number is negative, positive or zero.
a=float(input("Enter a no:"))
if a>0:
    print("Given No. is Positive")
elif a<0 :
    print("Given No. is negetive")
else:
    print("Given No. is Zero")
#Write a program to check whether a number is divisible by 5 and 11 or not.
b=int(input("Enter a no:"))
if b%5==0 and b%11==0:
    print("The Given no. is divisible by 5 and 11")
else:
    print("Given no. is not divisible by 5 and 11")
