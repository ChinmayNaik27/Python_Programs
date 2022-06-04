from random import *
from time import *
while True:
    random=randint(1,3)
    if random==1:
        print('RED')
        sleep(2)
        n=input('Wish to continue??:(y/n):')
        if n=='n':
            break
    elif random==2:
        print('VOILET')
        sleep(2)
        n=input('Wish to continue??:(y/n):')
        if n=='n':
            break
    elif random==3:
        print('GREEN')
        sleep(2)
        n=input('Wish to continue??:(y/n):')
        if n=='n':
            break
    else:
        print('No Value!!')
print('BBYE!!')
input()
