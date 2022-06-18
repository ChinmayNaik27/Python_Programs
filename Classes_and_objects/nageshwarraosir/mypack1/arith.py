# this is a module
import functools
def add(*vars):
    c=sum(vars)
    print("Sum is:",c)
def sub(*var):
    c=functools.reduce(lambda x,y:x-y,var)
    return c