#program to check whether a number is negative, positive or zero.
a=float(input("Enter a no:"))   # take string input form user and convert to Float value
if a>0:                               #If true=execute, if false move to elif loop
    print("Given No. is Positive")
elif a<0 :                           #if true execute and end , if false move to else
    print("Given No. is negetive")
else:                                #executes when if and elif both are false
    print("Given No. is Zero")