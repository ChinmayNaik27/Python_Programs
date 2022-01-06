"""WAP to Solve a code consider only keyboard keys (do not Consider tab,capslock,space,shift,alt control enter backspace)
i.e i/p is 1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,,./
if input is given O S, GOMR
o/p sholud be IAMFINE
"""
words="1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
s1=input("Enter code:")
s1=s1.upper()
arr=s1.split(" ")
s2=""
for x in arr:
    for y in x:
        i=words.index(y)
        s2+=words[i-1]
print(s2)