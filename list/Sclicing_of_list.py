##accessing list by Slicing
list1=[10,20,30,40,50,60,70,80,90]
print(list1)
print(list1[2:8])                     #print from index range 2 to 7
print(list1[2:8:2])                   #print from index range 2 to 7 with step 2
print(list1[2:])                      ##print from index range 2 (to right)
print(list1[:5])                       #print from index range 4 to it's left
print(list1[::2])                      #print complete list with step 2
print(list1[::-1])                     #print complete list in reverse