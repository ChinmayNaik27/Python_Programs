"""Write a Python program to create a shallow copy of sets.
Note : Shallow copy is a bit-wise copy of an object.
A new object is created that has an exact copy of the values in the original object."""
s1={10,20,30,40,50,60,70,80}
print(s1)
print(id(s1))
s2=s1
print(id(s2))
s2=s1.copy()
print(s2)
print(id(s2))