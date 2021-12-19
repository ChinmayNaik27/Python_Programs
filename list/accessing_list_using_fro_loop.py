#Accessing list using for loop
list1=[10,20,30,40]
for x in list1:
    print(x)        #print for every vslue of x
print("==========================================")
#2nd way
for i in range(0,len(list1)):
    print(list1[i])  #print for every value of i
print("===========================================")
#3rd way
for j in range(len(list1)):
    print(list1[j])   #print for every value of j