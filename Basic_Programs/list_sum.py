
list1 =[]
x= int(input())
y = int(input())
z = int(input())
n = int(input())
temp = []
sum = 0
for x1 in range(x + 1):
    for y1 in range(y + 1):
        for z1 in range(z + 1):
            list1.append([x1, y1, z1])
for q in list1:
    for r in q:
        sum = sum + r
    if sum != n :
        temp.append(q)
        sum=0
    else:
        sum=0

print(temp)