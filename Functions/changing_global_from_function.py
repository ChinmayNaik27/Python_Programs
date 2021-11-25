#Global value change from function:
#Global variable
x=10
def show():
    global x           #defining global x
    x+=1               #increment x by 1
    print(x)

print(x)