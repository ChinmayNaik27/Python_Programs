import os                                                  #module for working with files and folders
import shutil                                              #module for date and time
##methord 1.##
a=os.getcwd()                                         #gives the current working path or directory
print("Current directory  is:",a)
##methord 2. chdir()##
a=os.chdir("E:/Pyhton Assignments/test")               #ch directory to given path
a=os.getcwd()                                           #gives the current working path or directory
print("Now the path is :",a)
##methord 3.mkdir()##
os.mkdir("test1")                                       #makes directory or folder
##methord 4.makedirs()##
os.makedirs("a/b/c/d")                                 #makes multiple directories
##methord 5.rename()##
os.rename("test1","Test1")                              #renames folder
##methord 6.rmdir()##
os.rmdir("Test1")                                      #removes empty folder or directories
##methord 7.listdir()##
q=os.listdir()                                         #reads the folders in cwd
for a in q:
    print(a)
##Shutil##
shutil.rmtree("a")                                    #removes non- empty folders or direcotires