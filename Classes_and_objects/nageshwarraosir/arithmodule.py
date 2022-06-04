class arithmodule:
    def add(self,a=0,b=0,c=0,d=0,e=0):
        sum=a+b+c+d+e
        return sum
    def sub(self,a=0,b=0,c=0,d=0,e=0):
        sub=a-b-c-d-e
        return sub
    def mul(self,a=1,b=1,c=1,d=1,e=1):
        mul=a*b*c*d*e
        return mul
    def div(self,a=1,b=1,c=1,d=1,e=1):
        divint=(((a//b)//c)//d)//e
        return divint
    def divfloat(self,a=1,b=1,c=1,d=1,e=1):
        div=(((a/b)/c)/d)/e
        return div
    def sqroot(self,a):
        sqroot=a**0.5
        return sqroot
    def factorial(self,a):
        i=1
        c=1
        while i<=a:
            factorial=c*i
            i+=1
        return factorial
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