def show1(abc):
    return abc() + ' ' + 'Buddy'
def show():
    return 'Sam'

r=show1(show)
print(r)