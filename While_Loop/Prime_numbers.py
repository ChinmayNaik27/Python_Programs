# WAP to take a no. from user and print weather it is prime number or not
n=int(input("Enter a no:"))                                 #input from user and convert it to int
i=2                                                       #intialize i=2
while i<n:
     if n%i==0:
         print("Not a Prime No.")
         break                                             #to break the loop
     i += 1                                                #increment i by 1
if i==n:
        print("Prime No:",n)

