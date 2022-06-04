"""Generating a sequence!!!"""

def seq1(m,n):
    while m<n:
        yield m
        m+=1

obj=seq1(20,30)
print(obj)                                     #displays Object value of x
for i in obj:
    print(i,end=' ')