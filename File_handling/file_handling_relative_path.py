#open a file
f1=open("demo.txt","r")
s1=f1.read(5)                                        #reads only 5 character
print(s1)
s1=f1.read()                                          #reads all remaining characters
print(s1)
#closing a file
f1.close()