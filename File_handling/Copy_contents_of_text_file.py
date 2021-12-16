#copy contents of demo file into demo1 file in recent path
#opening a file
f1=open("demo.txt","rb")                                       #opens demo file in readbinary format
f2=open("demo3.txt","wb")                                       #opens demo1 file in writebinary format
s1=f1.read()                                                    #contents of file are stored in s1
f2.write(s1)
print(s1)
#contents copied from demo pasted in demo3
"""Alternate code for same 
lines=f1.readlines()
f1.write(lines)"""
#closing a file
f1.close()
f2.close()