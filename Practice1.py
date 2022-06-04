# """"""
#
# if __name__ == '__main__':
#     rec=[]
#     records=[]
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         rec.append(name)
#         rec.append(score)
#         records.append(rec)
#         rec=[]
#         temp=[]
#         temp1=[]
#     for i1 in records:
#         for j in records:
#             if i1[-1]==j[-1] and i1[-2] != j[-2]:
#                 temp.append(i1[-2])
#                 temp.append(j[-2])
#                 temp.sort()
#                 for i2 in temp:
#                     if i2 not in temp1:
#                         temp1.append(i2)
#     for i in temp1:
#         print(i)
#
# Result =[]
# scorelist = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input("Enter:")
#         score = float(input())
#         Result+=[[name,score]]
#         scorelist+=[score]
#     b=sorted(list(set(scorelist)))[1]
#     for a,c in sorted(Result):
#         if c==b:
#             print(a)
Result=[]
score1=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    Result+=[[name,score]]
    score1+=[score]
b=sorted(list(set(score1)))[1]
for a,c in sorted(Result):
    if c==b:
        print(a)
print(Result)
print(score1)
print(b)