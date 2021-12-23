############################Deletation or removal of items from list and indexing ############################3
list1=[100, 10, 20, 30, 40, 20, 20, 1.2, 'abc', [1, 2, 3], 1, 4, 5, 6]
print("================================remove()==========================")
list1.remove(1.2)
print(list1)
print("================================pop()==============================")
list1.pop(0)
print(list1)
print("========================indexing()=================================")
x=list1.index(20)
print(x)
x1=list1.index(20,2)
print(x1)
print("==============================count()================================")
y=list1.count(20)
print(y)
print("==============================print index values of 20===================")
for i in range (len(list1)):
    if list1[i]==20:
        print(i)
print("==============================clear()===============================")
list1.clear()
print(list1)


