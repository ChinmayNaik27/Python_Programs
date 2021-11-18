"""Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F """
f=int(input("Enter Grand Total:"))               #this is used to take the max marks obt in all subjects
phy=float(input("Enter marks for Physics:"))    # take string input form user and convert to Float value
chm=float(input("Enter marks for Chemistry:"))  # take string input form user and convert to Float value
bio=float(input("Enter marks for Biology:"))    # take string input form user and convert to Float value
math=float(input("Enter marks for Mathematics:"))  # take string input form user and convert to Float value
comp=float(input("Enter marks for Computer:"))    # take string input form user and convert to Float value
percent=((phy+chm+bio+math+comp)/f)*100           #Calulate % by addition of all input values / grand total *100
if percent >= 90:
    print("Grade A")
elif percent >= 80:
    print("Grade B")
elif percent >= 70:
    print("Grade C")
elif percent >= 60:
    print("Grade D")
elif percent >= 40:
    print("Grade E")
elif percent <= 40:
    print("Grade F")