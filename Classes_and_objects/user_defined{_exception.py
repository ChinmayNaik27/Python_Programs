#WAP to create user defined exception
class MyException(Exception):
    def __init__(self,msg):
        self.msg=msg
phone=input("Enter your Phone number:")

try:
    if len(phone)!=10:
        raise MyException("Phone No is less than 10 digits")
    print("Vaild Number:",phone)
except MyException as e:
    print(e)
