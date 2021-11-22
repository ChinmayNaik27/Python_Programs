#WAP to Calculate the result of a^b as per user
a=int(input("Enter Base No:"))                #taking input from user and convert it to integer
b=int(input("Enter Power No:"))               #taking input from user and convert it to integer
i=1
c=1
while i<=b:
    c=c*a                                      #multiply a and c and store result in c
    i+=1                                      #increment i by 1
print("Result is:",c)