"""Write a Python program to shuffle and print a specified list. """
list1=[10,20,30,40,50,60,70,80]
import random
for i in range(len(list1)):
    number=random.randint(0,i+1)
    list1[i],list1[number]=list1[number],list1[i]
print(list1)