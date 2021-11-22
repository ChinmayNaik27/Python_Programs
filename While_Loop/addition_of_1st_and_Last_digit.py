# WAP to take a no and Print addition of 1st and last no.
a=int(input("Enter a No for Addition of its 1st and last Digits: "))       #input from user and convert it to int
b=a%10                            #store last number in b
while a>9:
    a=a//10
a=b+a                            #add 1st and last no
print("Addition of its 1st and last Digit:",a)
