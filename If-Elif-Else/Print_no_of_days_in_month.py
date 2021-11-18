#Write a program to input month number and print number of days in that month.
mnt=int(input("Enter month no (From 1-12):")) # take string input form user and convert to Integer value
if mnt==1 or mnt==3 or mnt==5 or mnt==7 or mnt==8 or mnt==10 or mnt==12:  #all months with 31 days
    print("Entered no of month has 31 Days")
elif mnt==2:                                                              #as it has 28 days and 29 in leap year
    print("Entered no of month has 29 days if leap yr and 28 days if no leap year ")
else:
    print("Entered no of month has 30 Days")