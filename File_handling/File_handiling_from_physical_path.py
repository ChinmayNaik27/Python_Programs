#WAP for file handling using a file on hardisk

#open a file
f1=open("E:\\Pyhton Assignments\\dummy.txt","r")         #reads file on this location on hard disk
s1=f1.read(5)                                        #reads only 5 character
print(s1)
s1=f1.read()                                          #reads all remaining characters
print(s1)
#closing a file
f1.close()