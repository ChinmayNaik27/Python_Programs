import mypack.new2 as new2
x=new2.add(10,20,30)
print(x)
y=new2.sub(30,20)
print(y)


"""lambda function
write a lambda to find a square value of a number"""
def square(x):
    return x*x
f=square(4)
print(f)
#eqivalent lambda function
x=lambda x:x*x
y=x(4)
print(y)
print(x(10))

#lambda to find sum of 2 numbers

def sum_two(a,b):
    c=a+b
    return c

x=sum_two(10,15)
print(x)

# by lambda function
y=lambda a,b=0:a+b
print(y(15))

#even odd using lambda
x=lambda x:"even" if x%2==0 and x!=0 else "Not even"
print(x(3))

####
lst=[10,20,30,40,50,60,-10,-20,-30]
lst1=filter(lambda x:x%2==0,lst)
print(lst1)
for i in lst1:
    print(i,end=' ')
print("++++++++++++++++++++++++++")
lst1=list(filter(lambda x:x%2==0,lst))
print(lst1)


# using map function
lst=[10,20,30,40,-10]
x=map(lambda x:x*x,lst)
for i in x:
    print(i,end=' ')
print()
# x=list(x)   #or
x=list(map(lambda x:x*x,lst))
print(x)