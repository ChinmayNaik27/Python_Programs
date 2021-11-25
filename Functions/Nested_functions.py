"""Program for nested functions"""
#defining functions
def outer():
    print("hello")
    def inner():
        print("Buddy")
    inner()                                 #calling inner function
#calling Functions
outer()
print(outer.__doc__)                 #to see Parametrs