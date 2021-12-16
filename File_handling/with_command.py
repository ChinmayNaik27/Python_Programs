#WAP Using with Command

with open("demo.txt","rb") as e1:
    s1=e1.readlines()                                           #reads all lines from demo file
    for x in s1:
        print(x)