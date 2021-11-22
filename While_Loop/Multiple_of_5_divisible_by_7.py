"""Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
 (both included)"""
i=1500                                          #assign i to 1500
print("Nos Divisible by 7 and multiple of 5 are:")
while i<=2700:
    if i%5==0:                                 #for i multiple of 5
        if i%7==0:                             #multiple of 7
            print(i)
    i+=1                                       #increment of 1 in i

#2nd Methord:
"""i=1500                                          #assign i to 1500
print("Nos Divisible by 7 and multiple of 5 are:")
while i<=2700:
    if i%5==0 and i%7==0:                         #for i multiple of 5 and 7
        print(i)
    i+=1"""                                         #increment of 1 in i