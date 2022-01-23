#Combination of Conditional and default parametrs
def sample(x,y,z=10,w=20):
    c=x+y+z+w
    d=x*y*z*w
    e=x/y/z/w
    f=x*y-z/w
    return c,d,e,f

p,q,r,s=sample(10,90)
print(p,q,r,s,end="",sep=" Next ")