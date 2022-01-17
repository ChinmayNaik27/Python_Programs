#WAP to calculate the numeric ,Uppercase,lowercase letters given in userdefined string
s1=input("Enter a String:")
x1=0
y1=0
z1=0
w1=0
for x in s1:
    y=ord(x)
    if y>=48 and y<=57:
        x1+=1
    elif y>=65 and y<=90:
        y1+=1
    elif y>=97 and y<122:
        z1+=1
    else:
        w1+=1
print(f"The number of capital letters are {y1} , small letters are {z1} ,numerics are {x1},and special Symbols are {w1}")