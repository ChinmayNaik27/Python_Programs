if __name__ == '__main__':
    l=[]
    a=input()
    arr=a.split(" ")
    for i in range(len(arr)):
        if arr[i] < max(arr):
            l.append(arr[i])
    print(max(l))
#     n = int(input())
#     a=input("Enter values:")
#     arr = a.split(" ")
#     # arr.sort()
#     print(arr)
#     temp=[]
# for x in range(len(arr)):
#     if arr[x] not in temp:
#         temp.append(arr[x])
# temp.sort()
# print(temp)
# print(temp[-2])