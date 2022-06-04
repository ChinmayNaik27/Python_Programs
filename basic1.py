"""Calculator Program"""
print("Welcome !! Opertions performed are:\n1.Add\n2.Sub\n3.Mul\n4.Div1\n5.Div2")
try :
    while True:
        a=input("Enter a operation to be performed:")
        a=a.upper()
        b=int(input("Enter 1st number:"))
        c=int(input("Enter 2nd number:"))
        d=0
        if a=='ADD':
            d=b+c
            print("Addition is :",d)
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
        elif a=='SUB':
            d=b-c
            print("Substraction is :",d)
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
        elif a=='MUL':
            d=b*c
            print("Multiplication is :",d)
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
        elif a=='DIV1':
            d=b/c
            print("Division1 is :",d)
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
        elif a=='DIV2':
            d=b//c
            print("Division2 is :",d)
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
        else:
            print("Operation listed is not performed!!")
            print("Please select operation given in the list")
            a1=int(input("Press 1 to continue\nanyother key to exit:"))
            if a1!=1:
                break
except ValueError as e2:
    print('Chao!!')
    input('Press q to exit!!')        #this is to hold screen output
