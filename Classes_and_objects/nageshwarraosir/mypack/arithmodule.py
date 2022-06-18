from functools import *
class arithmodule:
    def add(self,*para):
        sum1=sum(para)
        return sum1
    def sub(self,*name):
        sub=reduce(lambda x,y:x-y,name)
        return sub
    def mul(self,a=1,b=1,c=1,d=1,e=1):
        mul=a*b*c*d*e
        return mul
    def div(self,*tup):
        divint=reduce(lambda x,y:x//y,tup)
        return divint
    def divfloat(self,*tup1):
        div=reduce(lambda x,y:x/y,tup1)
        return div
    def sqroot(self,a):
        sqroot=a**0.5
        return sqroot
    def fact(self,a):
        if a==0:
            res=1
        else:
            res=a * self.fact(a-1)
        return res
    def fibonicii(self,limit):
        x1=0
        x2=1
        i=0
        while i<limit:
            print(x1,end=' ')
            fb=x1+x2
            x1=x2
            x2=fb
            i+=1
arithmod=arithmodule()