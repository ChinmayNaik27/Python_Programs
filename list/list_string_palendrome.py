#WAP to take a list which contain string and print only those strings which is palendrome
list1=['civic','gone','radar','madam','refer','mobile','racecar','tacocat','oppo']
x=len(list1)
print(x)
for i in list1:
    if i==i[::-1]:
        print(i)