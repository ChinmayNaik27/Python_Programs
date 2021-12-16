#WAP to determine position of pointer in file while executuion

with open("demo.txt","rb") as f1:
    x=f1.tell()
    print("Position:",x)
    s1=f1.read(3)
    x1=f1.tell()
    print("Position:",x1)
#####using seek######
with open ("demo.txt","rb") as e1:
    e1.seek(4,0)                        #displays 4 characters from beginning
    x = e1.tell()
    print("Position:", x)
    w=e1.seek(6,1)                       #displays  characters from current position
    x = e1.tell()
    print("Position:", x)
    w=e1.seek(-9,2)                     #displays last nine characters
    x = e1.tell()
    print("Position:", x)
    print(e1.read())