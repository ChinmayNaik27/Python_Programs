"""Defining functions for arithimatic operations and call them"""
#Defining Functions
def add():
    a=int(input ("Enter 1st no:"))
    b = int(input("Enter 2st no:"))
    z=a+b
    print("Addition:",z)
def sub():
    a=int(input ("Enter 1st no:"))
    b = int(input("Enter 2st no:"))
    z=a-b
    print("Substration:",z)
def mul():
    a=int(input ("Enter 1st no:"))
    b = int(input("Enter 2st no:"))
    z=a*b
    print("Multiplication:",z)
def divide():
    a=int(input ("Enter 1st no:"))
    b = int(input("Enter 2st no:"))
    z=a/b
    print("Division:",z)
def mod():
    a=int(input ("Enter 1st no:"))
    b = int(input("Enter 2st no:"))
    z=a%b
    print("Mod:",z)
#Calling a Function
add()
sub()
mul()
divide()
mod()
