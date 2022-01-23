#print hello only once each time the function is called

def getvalue(mylist=None):
    if mylist==None:
        mylist=[]
        mylist.append('Hey')
    return mylist
print(getvalue())
print(getvalue())
print(getvalue())