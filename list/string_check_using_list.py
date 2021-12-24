"""WAP to take a list and print addition of all elements print only those items whose length is > 2 and
their 1st and last character of string is same"""
list1=['abc','aca','xyx','zyz','dty','uzu','ity','ooo']
list2=[]
for x in list1:
    if len(x)>2 and x[0]==x[-1]:
        list2.append(x)
print(list2)
for i in list2:
    print(i)