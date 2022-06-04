def show1(abc):
    r=abc()
    return r + ' ' + "Buddy"
def show():
    return "Ram"

r=show()
r1=show1(show)
print(r1)