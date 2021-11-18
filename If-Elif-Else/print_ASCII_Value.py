#Program to print ASCII Value:
q=input("Enter q for acii value table:")  # take string input form user
if q=='q':
 for i in range (1,255):                #for every value of i ranging from 1 to 255
        print(i,"=",chr(i))             #print value of i  then = then convert ASCII to character
else:
    print("Okay have a Good Day")