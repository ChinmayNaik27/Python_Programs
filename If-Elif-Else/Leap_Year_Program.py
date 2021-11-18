#Write a program to check whether a year is leap year or not.
a=input("enter a year:") # take string input form user
a=int(input("Enter No Of Days of Present year:")) # take string input form user and convert to Integer value
if a==366:                             #as Leap year has 366 days
    print("This year is a leap year")
else:
    print("This is not a leap year")
