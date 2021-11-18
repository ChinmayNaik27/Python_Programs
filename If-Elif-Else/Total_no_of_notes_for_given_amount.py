#Write a program to count total number of notes in given amount
amt=int(input("Enter Amount Recived:")) # take string input form user and convert to Integer value
if amt>=10 and amt<=20:
    amt=amt//10                                   #to Obtain Integer value // is used
    print("10 Notes are:",amt)
elif amt>=20 and amt<=50:
    amt=amt//20
    print("20 Notes are:",amt)
elif amt>=50 and amt<=100:
    amt=amt//50
    print("50 Notes are:",amt)
elif amt>=100 and amt<=500:
    amt=amt//100
    print("100 Notes are:",amt)
elif amt>=500 and amt<=2000:
    amt=amt//500
    print("500 Notes are:",amt)
else:
    amt=amt//2000
    print("2000 notes are:",amt)
#2nd way (this shows every possible no of notes required for given amount):
amt=int(input("Enter Amount Recived:"))                # take string input form user and convert to Integer value
print("For the Given Amount, The Notes can be:")
if amt>=10:
    note=amt//10
    print("10 Notes are:",note)
if amt>=20:
    note=amt//20
    print("20 Notes are:",note)
if amt>=50:
    note=amt//50
    print("50 Notes are:",note)
if amt>=100:
    note=amt//100
    print("100 Notes are:",note)
if amt>=500:
    note=amt//500
    print("500 Notes are:",note)
if amt>=2000:
    note=amt//2000
    print("2000 notes are:",note)