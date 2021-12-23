################Addition of items in list#############################

list1=[10,20,30,40,20]
##appending list
print("==============================append()=============================")
print(list1)
list1.append(20)
list1.append(1.2)
list1.append('abc')
list1.append([1,2,3])
print(list1)
print("===========================extend()=================================")
list1.extend([1,4,5,6])
print(list1)
print("============================insert()===============================")
list1.insert(0,100)
print(list1)
print("================================reverse()======================================")
list1.reverse()
print(list1)