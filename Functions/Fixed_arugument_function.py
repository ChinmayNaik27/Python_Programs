# Wap to print * by taking function form user using function:
#defining a Funtion.
def star(rows,columns):                       ## fixed arguments
    """
    :param rows: input parameter for rows
    :param columns: input parametrs for columns
    """
    #Defining Function
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            print("*",end=" ")
        print("")

#Calling  a Function
star(6,6)
print("==================================================")
star(6,5)
print("===================================================")
star(3,3)
print("====================================================")
star(3,6)