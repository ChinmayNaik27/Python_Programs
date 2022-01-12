"""Built-In Strings"""
s1="This is String1"
#####Capitalize
print(s1.capitalize())
#####Lower
print(s1.lower())
###########upper
print(s1.upper())
#########swapcase
print(s1.swapcase())
########count
s2="This is String2"
x=s2.count('is')
print(x)
x=s2.count('is',4)
print(x)
x=s2.count('is',4,6)
print(x)
########startswith
print(s2.startswith('T'))
print(s2.startswith('Th'))
print(s2.startswith('This'))
print(s2.startswith('This is'))
print(s2.startswith('T',4))
###endswith
print(s2.endswith('2'))
print(s2.endswith('g2'))
print(s2.endswith('ring2'))
print(s2.endswith('is String2'))
print(s2.endswith('d'))
