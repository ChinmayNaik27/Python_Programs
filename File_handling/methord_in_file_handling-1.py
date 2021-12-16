import os                                                  #module for working with files and folders
import datetime                                              #module for date and time
##methord 1. getsize##
a=os.path.getsize("demo.txt")                                         #gives size of file in bytes
print("Size in  bytes is:",a)
##methord 2. exisits()##
a=os.path.exists("demo.txt")                #ch directory to given path
print("The Given file is present.(True or False):",a)
##methord 3. isdir() and isfile()##
os.mkdir("test1")                                       #makes directory or folder
##methord 4.getctime() and getmtime()##
os.makedirs("a/b/c/d")                                 #makes multuple directories