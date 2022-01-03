#WAP to create a set and use set methords
#creating a set
s1={10,20,30,40,1.2,(1,2,3),'abc'}
print(type(s1))
print(s1)
s2={11,}            #set with 1 element
print(type(s2))
print(s2)
s3=set()            #empty set
print(s3)
###methords
##add
s3.add(15)
print(s3)
s1.add(100)
print(s1)
s1.add(985)
print(s1)
#update values
s1.update([1,2,3,4,5,6])
print(s1)
#remove
s1.remove(4)
print(s1)
#discard
s1.discard(6)
print(s1)
#Clear the set
s1.clear()
print(s1)