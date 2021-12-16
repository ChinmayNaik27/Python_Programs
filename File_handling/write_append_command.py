#WAP to wirte and append lines using relative path

#open a file
f1=open("demo.txt","r")
s1=f1.readline(5)                                        #reads only 5 character in 1st line
print(s1)
s1=f1.readline()                                          #reads all remaining characters in 1st line
print(s1)
s1=f1.readlines()                                           #reads all the lines in list format
print(s1)
print(type(s1))                                             #shows type of s1
for x in s1:
    print(x)                                              #prints every element in list sepereately
#closing a file
f1.close()