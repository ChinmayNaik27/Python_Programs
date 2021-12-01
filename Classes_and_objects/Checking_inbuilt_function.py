#class for built in functions
class test():
    """
    This is a Test Class
    """
    def __init__(self,x,y):
        """
        :param x:This is x value
        :param y: This is y value
        """
        self.x=x
        self.y=y
    def show(self):
        """
        :return:Gives addition
        """
        print(self.x+self.y)
a=test(100,200)
a.show()
print(test.__name__)
print(test.__module__)
print(test.__bases__)
print(dir(a))
print(a.__dir__)
print(test.__doc__)
print(test.__init__.__doc__)
print(a.show.__doc__)
