# # # class A:
# # #     def __init__(self):
# # #         self.i=10
# # # class B(A):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.j=10
# # #     def add(self):
# # #         self.z=self.i+self.j
# # #         return self.z
# # #
# # # ob=B()
# # # print(ob.add())
# # #
# # class A:
# #     def __init__(self,p,q):
# #         self.i=p
# #         self.j=q
# # class B(A):
# #     def __init__(self,a,b):
# #         super().__init__(a,b)
# #     def add(self):
# #         self.z=self.i+self.j
# #         print(self.z)
# #     def __str__(self):
# #         return "Thiss is Class Derived class of A"
# # class C(A):
# #     def __init__(self,a1,b1):
# #         super().__init__(a1,b1)
# #     def combo(self):
# #         self.z1=self.i-self.j
# #         print(self.z1)
# # ob=B(10,20)
# # ob.add()
# # ob1=C(40,20)
# # ob1.combo()
# # print(B(10,20))
# class B:
#     def __init__(self,a,b):
#         self.i=a
#         self.j=b
#     def add(self):
#         self.z=self.i+self.j
#         print(self.z)
#     def __str__(self):
#         return "Thiss is Class Derived class of A"
#
# def object(ob1):
#     if hasattr(ob1,'add'):
#         ob.add()
#     else:
#         print("No methord!!")
# ob=B(20,30)
# object(ob)
class exp(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    phone=input("Enter Your Phone number:")
    if len(phone)!=10:
        raise exp("Phone != 10")
    print(phone)
except exp as e:
    print(e)
f1=open('file1.py ')
a=f1.read()
print(a)