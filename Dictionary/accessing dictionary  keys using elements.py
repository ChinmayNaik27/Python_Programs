"""Write a Python program to access dictionary keys element by index. """
dict1={1:20,2:'abc',3:1.2,4:'ppp'}
dkeys=dict1.keys()
print(dkeys)
for x in dkeys:
    print(" The Keys are :",x,end="")
dval=dict1.values()
print('\n',dval)
for x1 in dval:
    print(" The Values Of Keys Are:",end="")