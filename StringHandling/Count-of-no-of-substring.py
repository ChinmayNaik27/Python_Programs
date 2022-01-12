#WAP to count all the number of substring in given sting
#sample s1="This is Demo"
#output for is is 2
s1="This is a demo ,This is a String"
x=-1
while True:
    x=s1.find('is',x+1)
    if x==-1:
        break
    print(x)