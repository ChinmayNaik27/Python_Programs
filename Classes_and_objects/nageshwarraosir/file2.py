# # a=int(input("Ente a nu:"))
# # a1=a
# # sum=0
# # while a>0:
# #     b=a%10
# #     sum=sum+b
# #     a=a//10
# # print("Total is:",sum)
# #
# # b1=a1%10
# #
# #     a1=a1//10
# # sum=b1+a1
# # print(sum)
# #
# # i=0
# # n1=0
# # n2=1
# # while i<=51:
# #     print(n1)
# #     fb=n1+n2
# #     n1=n2
# #     n2=fb
# #     i+=1
# #
# # a=input("Enter base value:")
# # s4=""
# # s1=a[0]
# # s2=a[-1]
# # s3=a[1:len(a)-1]
# # s4=s2+s3+s1
# # s4=int(s4)
# # print(s4)
class A:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    @classmethod
    def from_string(cls,s1):
        d,m,y=map(int,s1.split('-'))
        date1=cls(d,m,y)
        return date1
    @staticmethod
    def date3(msg2):
        d,m,y=map(int,msg2.split("-"))
        if d>=1 and d<=31 and m>=1 and m<=12:
            return True
        else:
            return False
    def show(self):
        print(f"Date:{self.d}",f"Month:{self.m}",f"Year:{self.y}",sep='\n')
ob=A(10,20,30)
ob.show()
ob1=A.from_string("12-03-20")
ob1.show()
if A.date3("12-03-21"):
    print("Vaild")
else:
    print("Invaild")
# class Mydate:
#     def __init__(self,d,m,y):
#         self.day=d
#         self.month=m
#         self.year=y
#     @classmethod
#     def from_string(cls,s1):
#         d,m,y=map(int,s1.split('-'))
#         date1=cls(d,m,y)
#         return date1
#     @staticmethod
#     def is_vaild_date(s1):
#         d,m,y=map(int,s1.split('-'))
#         if (d>=1 and d<=31) and (m>=1 and m<=12):
#             return True
#         else:
#             return False
#     def show(self):
#         print(self.day,self.month,self.year)
# d1=Mydate(10,12,2021)
# d1.show()
# d2=Mydate.from_string("1-11-2020")
# d2.show()
# if Mydate.is_vaild_date("4-12-2021"):
#     print("Vaild")
# else:
#     print("Invaild")