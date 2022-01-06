#Arrange hte given string in accending ordr but the numeric in string should be at last
s1="15this34"
print(s1)
list1=list(s1)
list1.sort()
s2="".join(list1)
print(s2)
y=0
for i in range(len(s2)):
    x=ord(s2[i])
    if x>=48 and x<=57:
        y=i
print(y)
s3=s2[0:y+1]
s4=s2[y+1:]
s5=s4+s3
print(s5)