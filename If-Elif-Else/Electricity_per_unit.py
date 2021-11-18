"""Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
"""
print("This is To Calculate Electricity Bill Per Unit Consumed:")
a=float(input("Input the Units Of Energy Consumed:"))  # take string input form user and convert to Float value
if a<=50:
    total=a*0.50
    s=total*0.2                                    #surplus amount
    print("Total Cost for Energy Consumed is:",total+s)  #added surplus with total
elif a>=50 and a<=150:
    total=a*0.75
    s = total * 0.2
    print("Total Cost for Energy Consumed is:", total + s)
elif a>150 and a<=250:
    total=a*1.20
    s = total * 0.2
    print("Total Cost for Energy Consumed is:", total + s)
elif a>250:
    total=a*1.50
    s = total * 0.2
    print("Total Cost for Energy Consumed is:", total + s)