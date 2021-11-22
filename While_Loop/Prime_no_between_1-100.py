# WAP to Print all prime numbers from 1 to 100
print("Prime Nos From 1 to 100 Are:")
a=1                                         #intialize a=1
while a<=100:
    i=2
    while i<a:
        if a%i==0:
            break                            # to break loop
        i+=1
    if i==a:
        print("Prime No :",i)

    a+=1                                      #increment a by 1
print("Loop End")