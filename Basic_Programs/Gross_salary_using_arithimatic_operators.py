#gross using arithimatic operators
bs=float(input("Input Your Basic Salary:"))     #take input form user in integer format
da=0.4*bs                                       # as 40% of base salary is da
hra=0.2*bs                                       # as 20% of base salary is hra
gross=bs+da+hra                                  #Total salary is addition of da,hra and basic salary
print("Your Gross Salary Is :",gross)