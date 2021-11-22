#WAP to take input from user and print its factorial
a=int(input("Enter a number for factorial:"))    #taking input from user and convert it to integer
i=1                                              #initalizing i=1
b=1                                              #initalizing b=1
print("Entered no is :",a)
while i<=a:
    b=b*i                                         #multiply b*c and store it in b
    i+=1                                         #increment i by 1
print("Factorial:",b)