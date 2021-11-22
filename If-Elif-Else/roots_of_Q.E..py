#Write a program to find all roots of a quadratic equation.
import math                                                   #importing math function for sq root
print("A Q.E Is In The Form Of ax^2 + bx + c = 0")
a=float(input("Enter the value of a (i.e perfix of x^2):"))  # take string input form user and convert to Integer value
b=float(input("Enter the value of b (i.e prefix of x):"))    # take string input form user and convert to Integer value
c=float(input("Enter the value of c:"))                      # take string input form user and convert to Integer value
root=(b*b)-4*a*c
if root<0:
   root=abs(root)                                               #converting to positive value if negetive using abs
f=math.sqrt(root)
q1=(-b-f/2*a)
q2= (-b+f/2*a)
print("Roots are:",q1,"\n",q2)

#2nd way:
import cmath                                                  #importing cmath function for complex no
print("A Q.E Is In The Form Of ax^2 + bx + c = 0")
d=float(input("Enter the value of a (i.e perfix of x^2):"))  # take string input form user and convert to Integer value
e=float(input("Enter the value of b (i.e prefix of x):"))    # take string input form user and convert to Integer value
f=float(input("Enter the value of c:"))                      # take string input form user and convert to Integer value
root=(e*e)-4*d*f
g=cmath.sqrt(root)                                            #Taking sq root
q1=(-b-g/2*a)
q2= (-b+g/2*a)
print("Roots are:",q1,"\n",q2)

