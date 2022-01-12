class exception(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    a=int(input("Enter a no1:"))
    b=int(input("Enter a no2:"))
    ans=a+b
    if ans<0:
        raise exception("N.A")
    print(ans)
except exception as e1:
    print(e1)