if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lst=[]
    lst+=student_marks.get(query_name)
    a,b,c=lst[0],lst[1],lst[2]
    avg=(a+b+c)/3
    print(avg)