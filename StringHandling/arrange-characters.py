#WAP to take input from user and arrange the numeric in the last of the string and display
#sequence:1st uppercase,2nd lowercase,3rd symbols,4th numeric
s1=input("Enter String:")
s2=""
s3=""
s4=""
s5=""
for x in s1:
    y=ord(x)
    if y>=48 and y<=57:
        s2+=x
    elif y>=65 and y<=90:
        s5+=x
    elif y>=97 and y<=122:
        s4+=x
    else:
        s3+=x
print(s5+s4+s3+s2)