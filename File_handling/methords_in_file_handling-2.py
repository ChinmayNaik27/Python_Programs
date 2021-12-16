import os                                                  #module for working with files and folders
import datetime                                              #module for date and time
##methord 1. getsize##
a=os.path.getsize("demo.txt")                                         #gives size of file in bytes
print("Size in  bytes is:",a)
##methord 2. exisits()##
a=os.path.exists("demo.txt")                #checks file is present or not
print("The Given file is present.(True or False):",a)
##methord 3. isdir() and isfile()##
a=os.path.isdir("demo.txt")                                       #checks it is directory or not
print("The Given file is a directory.(True or False):",a)
a=os.path.isfile("demo.txt")                                      #checks it is file or not
print("The Given file is in fileformat.(True or False):",a)
##methord 4.getctime() and getmtime()##
a=os.path.getctime("demo.txt")                                       #gets the creation time of file
print("Time in microseconds is :",a)
t1=datetime.datetime.fromtimestamp(a)                               #converts microseconds in date and time format
print("Output in Date and Time Format is:",t1)
a=os.path.getmtime("demo.txt")                                       #returns / gets modified time of the given file
print("Time in microseconds is :",a)
t1=datetime.datetime.fromtimestamp(a)                                 #converts microseconds in date and time format
print("Output in Date and Time Format is:",t1)
