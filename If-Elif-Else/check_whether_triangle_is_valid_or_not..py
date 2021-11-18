#Write a program to input angles of a triangle and check whether triangle is valid or not.
a=float(input("Enter 1 st angle of triangle:"))     # take string input form user and convert to Float value
b=float(input("Enter 2 nd angle of triangle:"))     # take string input form user and convert to Float value
c=float(input("Enter 3 rd angle of triangle:"))     # take string input form user and convert to Float value
if (a and b and c) == 60:
    print("It is an equilateral triangle")
elif (a and b and c)<=180:               #as Sum of all angles of Triangle is 180
    print(" It is a triangle")
else:
    print("Its not a triangle")
