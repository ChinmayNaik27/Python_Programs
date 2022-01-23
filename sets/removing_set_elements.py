#5. Write a Python program to remove an item from a set if it is present in the set.

set={10,20,30,40,50,60,70,90}
print(set)
print(len(set))
print(max(set))
print(min(set))
x=int(input("Enter a number:"))
if x in set:
    set.remove(x)
    print(set)
    print(len(set))
else:
    print("Element not present in set!!!")