#WAP to take input from user and print its table
n=int(input("Enter the no for which you want the table:")) #taking input from user and convert it to integer
print("The Table for given no. is:\n")                  #\n  is to shift output on new line
i=1                                                     #initalizing i=1
while i<=10:
    b=n*i                                               #store n*i in b
    print(n,"*",i,"= ",b)
    i+=1                                                 #increment i