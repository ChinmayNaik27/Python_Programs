""". Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

list1=['Red', 'Green', 'White', 'Black', 'Pink','Yellow']
list1.pop(0)
list1.pop(3)
list1.pop(3)
print(list1)