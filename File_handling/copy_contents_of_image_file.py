#Copy image file from 1 to another file
#opening file
a1=open("start-now-stop-never-2560x1440-1177.jpg","rb")
a2=open("copy_image.jpg","wb")
q=a1.read()                                                #read contents of a1 and store them in q
a2.write(q)                                                #write contents of q in a2
print("Success")
#closing files
a1.close()
a2.close()