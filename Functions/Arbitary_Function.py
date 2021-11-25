"""Arbiatry functions"""
#Defining Function
def show(*name):
    """
    :param name: string parameters stored
    """
    for n in name:
        print(n)
#calling Functions:
show("aabb","xyz","a","b","c")
show("and")
show("and","or")
#to Check Documentation of function
print(show.__doc__  )