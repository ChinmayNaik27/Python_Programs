"""
Create a global variable(means declare list at start of program) called myUniqueList. It should be an empty list to start.
Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList,
unless its value already exists in myUniqueList.
If the value doesn't exist already it should be added and the function should return True.
If the value does exist, it should not be added, and the function should return False;
Finally, add some code below your function that tests it out.
It should add a few different elements, showcasing the different scenarios,
and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:

Add another function that pushes all the rejected inputs into a separate global arraylist called myLeftovers.
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness),
it should get added to myLeftovers instead
"""
myuniquelist=[]
myleftovers=[]
def listappend():
    global myuniquelist
    x=input("Enter items:")
    if x not in myuniquelist:
        myuniquelist.append(x)
        return True
    else:
        myleftovers.append(x)
        return False
n=int(input("Enter number os items to be insetred in list1:"))
for x1 in range(n):
    listappend()
print(myuniquelist)
print("repeated Elements:\n",myleftovers)