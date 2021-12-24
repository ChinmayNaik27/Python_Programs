#WAP to take a list which contain string and print only those strings which is palendrome
list1=['civic','gone','radar','madam','refer','mobile','racecar','tacocat','oppo']
for i in list1:
    if (i[0] and i[1])==(i[-1] and i[-2]):
        print(i)