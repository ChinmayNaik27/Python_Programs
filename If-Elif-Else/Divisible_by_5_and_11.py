#Write a program to check whether a number is divisible by 5 and 11 or not.
b=int(input("Enter a no:"))
if b%5==0 and b%11==0:                  #executes if remainder when divided by 5 and 11 is zero
    print("The Given no. is divisible by 5 and 11")
else:
    print("Given no. is not divisible by 5 and 11")