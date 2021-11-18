#Maximum no from 3 nos.
c=int(input("Enter no1:"))    # take string input form user and convert to Integer value
d=int(input("Enter No2:"))    # take string input form user and convert to Integer value
e=int(input("Enter No3:"))    # take string input form user and convert to Integer value
print("Your Nos Are : ",a,"and ",b)
if c>=d and c>=e :
    print("A is Max")
elif d>=c and d>=e:
    print("B is Max")
else:
    print("C is Max")