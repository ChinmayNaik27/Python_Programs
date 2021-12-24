################copy#########333
list1=[10,20,30,40,50]
list2=list1                     #list 2 act as a duplicate or token name for list 1
list2[0]=123
print(list1)
print(list2)
print(id(list1))                  #sepcifiees the location at which list is stored
print(id(list2))
###################copying list########333
list4=[10,20,30,40,50]
list3=list4.copy()                  #copies the list and stores it in different location
list4[0]=123
print(list3)
print(list4)
print(id(list3))                 #shows memory address
print(id(list4))