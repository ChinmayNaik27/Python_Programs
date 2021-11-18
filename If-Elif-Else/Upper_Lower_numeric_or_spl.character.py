#program for character output:
f=ord(input("Enter a character:"))      # take string input form user and convert to ASCII value
if f>=48 and f<=57:
    print("Numeric No")
elif f>=65 and f<=90:

    print("Upper Case Letter")
elif f>=97 and f<=122:

    print("Lower Case Letter")

else:
    print("Entered No is spl character")