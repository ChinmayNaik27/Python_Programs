"""Write a program to input basic salary of an employee and calculate its Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%
"""
bs=float(input("Enter Your Salary:"))
if bs <= 10000:
    hra=0.2*bs
    da=0.8*bs
    bs=bs+hra+da
    print("Your Gross Salary is :",bs)
elif bs <= 20000:
    hra = 0.25 * bs
    da = 0.9 * bs
    bs = bs + hra + da
    print("Your Gross Salary is :", bs)
elif bs > 20000:
    hra = 0.3 * bs
    da = 0.95 * bs
    bs = bs + hra + da
    print("Your Gross Salary is :", bs)