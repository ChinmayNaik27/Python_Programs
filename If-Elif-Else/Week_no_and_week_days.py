#Write a program to input week number and print week day
wn=int(input("Enter week day no:")) # take string input form user and convert to integer value
if wn==7:
    print("Sunday")
elif wn==1:
    print("Monday")
elif wn==2:
    print("Tuesday")
elif wn==3:
    print("Wednesday")
elif wn==4:
    print("Thursday")
elif wn==5:
    print("Friday")
elif wn==6:
    print("Saturday")
else:
    print("Invalid Week No. Please Check")