#WAP to wirte and append lines using relative path

#open a file
f1=open("demo1.txt","w")                                              #writing text in file
f1.write("This is not a good gesture friend\n")
f1.write("why dont you take a leave \nit appers that you are sick ")
#closing a file
f1.close()
##appending a file:
#open a file
f1=open("demo1.txt","a")                                                  #addition of text in file
f1.write("You Should Visit a Doctor\n ")
f1.write("and take Complete Rest\n")
#closing a file
f1.close()