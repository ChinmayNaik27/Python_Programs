#Basics of Tuple
tuple1=(1,2,3,'abc',1,1.2,56)
print(tuple1)
x=tuple1.index(2)
print(x)
y=tuple1.count(1)
print(y)
#accessing tuple is same as list
print(tuple1[0])
print(tuple1[-1])
print(tuple1[2:5])
print(tuple1[:5])
print(tuple1[2:])
print(tuple1[::])
print(tuple1[::-1])
print(tuple1[:-1])
#creating a tuple with single element
t1=(100,) #tuple of single element
print(t1)
print(type(t1))
print(id(t1)) #shows location where it is stored