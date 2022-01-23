#without using Map function
def function1(list1):
    temp=[]
    for x in list1:
        temp.append(x*x)
    return temp
list1=[1,2,3,4,5,6,7,8,9,10]
a=function1(list1)
print(a)