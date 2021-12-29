#WAP of GUI For Check Box
#importing Libraries
from tkinter import *
def check():
    s1=""
    if v1.get()==1:
        s1+="C"
    if v2.get()==1:
        s1+=" CPP"
    if v3.get()==1:
        s1+=" Pyhton"
    l1['text']=s1
#Creating Root Object
root=Tk()
#setting Tittle
root.title("This is for taking input from user")
#changing Size of Window
root.geometry("500x500")
#creating frame window
f1=Frame(root,bg='pink',width=500,height=500)
f1.pack(fill='both',expand=True)
#additing checkbox
v1=IntVar()
c1=Checkbutton(f1,text='C',width=15,variable=v1)
c1.pack()
v2=IntVar()
c2=Checkbutton(f1,text='CPP',width=15,variable=v2)
c2.pack()
v3=IntVar()
c3=Checkbutton(f1,text="Python",width=15,variable=v3)
c3.pack()
#creating labels
l1=Label(f1,text="Result is here",font=("Arial",14,"italic"),bg="yellow")
l1.pack()
#creating buttons
b1=Button(f1,text='OK',width=20,command=check)
b1.pack()
#display window by using mainloop
root.mainloop()