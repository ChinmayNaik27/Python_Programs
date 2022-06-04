"""Calculator Program"""
print("Welcome !! Opertions performed are:\nAdd\nSub\nMul\nDiv1\nDiv2")
while True:
    a = input("Enter a operation to be performed:")
    a = str(a.upper)
    b = int(input("Enter 1st number:"))
    c = int(input("Enter 2nd number:"))
    d = 0
    if a == 'ADD':
        d = b + c
        print("Addition is :", d)
    elif a == 'SUB':
        d = b - c
        print("Substraction is :", d)
    elif a == 'MUL':
        d = b * c
        print("Multiplication is :", d)
    elif a == 'DIV1':
        d = b / c
        print("Division1 is :", d)
    elif a == 'DIV2':
        d = b // c
        print("Division2 is :", d)
    else:
        print("Operation listed is not performed!!")
        print("Please select operation given in the list")
        a1 = input("Press 1 to continue\nanyother key to exit:")
        if a1 != 1:
            break
