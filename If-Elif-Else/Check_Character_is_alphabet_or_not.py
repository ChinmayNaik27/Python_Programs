"""Write a program to check whether a character is alphabet or not"""
b=ord(input("Enter a character:"))         # take string input form user and convert to ASCII value
if b>=65 and b<=122:                  #if Both condition are true , execute(ASCII values of aplhabets is from 65 to 122
    print("Entered character is an alphabet")
else:                                  #executed when if is False
    print("Entered Character is not an alphabet")