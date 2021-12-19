#accessing list by negetive indexing
list1=[10,20,30,40,50,60,70,80,90]
print(list1)                                  #print complete list
print(list1[-1])                                 #print last index element of list
print(list1[-2])
print(type(list1))                            #print its class
print(list1[-2:-8:-1])                     #print from index range -2 to -7 with step -1
print(list1[-2:-8:2])                   #print from index range -2 to -7 with step +2
print(list1[-2:])                      ##print from index range 2 (to right)
print(list1[:-5])                       #print from index range 4 to it's left
print(list1[::-2])                      #print complete list with step 2
print(list1[:-5:-1])                     #print list from -5 to left eith step -1
print(list1[:-5:1])