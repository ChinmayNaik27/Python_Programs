class Mydate:
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y
    @classmethod
    def from_string(cls,s1):
        d,m,y=map(int,s1.split('-'))
        date1=cls(d,m,y)
        return date1
    @staticmethod
    def is_vaild_date(s1):
        d,m,y=map(int,s1.split('-'))
        if (d>=1 and d<=31) and (m>=1 and m<=12):
            return True
        else:
            return False
    def show(self):
        print(self.day,self.month,self.year)
d1=Mydate(10,12,2021)
d1.show()
d2=Mydate.from_string("1-11-2020")
d2.show()
if Mydate.is_vaild_date("4-12-2021"):
    print("Vaild")
else:
    print("Invaild")