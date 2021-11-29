#wap to take input form user and check it is even or not using lambda
a=int(input("Enter a number:"))
b=lambda a: "even" if a%2==0 else "Odd"
print(b(a))