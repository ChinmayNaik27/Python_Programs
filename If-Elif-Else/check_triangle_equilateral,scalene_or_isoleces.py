#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
d=float(input("Enter 1 st angle of triangle:")) # take string input form user and convert to Float value
e=float(input("Enter 2 nd angle of triangle:"))  # take string input form user and convert to Float value
f=float(input("Enter 3 rd angle of triangle:"))  # take string input form user and convert to Float value
if a+b+c==180:                                  #if sum of angles is 180 thenexectue if loop and check for conditions
    if (d and e and f) == 60:                   #executes if all 3 are 60
        print("Its an equilateral Triangle")
    elif (d == e) or (d == f) or (e == f):       #executes if any 2 sides are equal
        print("Its an Isoceles Triangle")
    elif (d != e != f):                          #executes when all are not equal
        print("Its a scalene triangle")
else:
    print("Invaild Angles Of Triangles.")