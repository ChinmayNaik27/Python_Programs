#layout Place-Manager
from tkinter import *
#creating root window
root=Tk()
#setting Title
root.title("This is frame ")
#change size
root.geometry("500x500")
#Frame Window
f1=Frame(root,bg="Orange",width=20,height=500)
#Additing it to root Window with position specified
f1.pack(fill=BOTH,expand=True)
#Creating Label
l1=Label(f1,text='Result',font=('Times New Roman',20,'bold'),bg='yellow')
l1.pack()
b1=Button(f1,text='OK',width=20)
#Additing it to root Window with Position Specified
b1.place(x=100,y=240)
b2=Button(f1,text='ppp',width=20)
#Additing it to root Window with value Y and side left and pad x
b2.place(x=100,y=200)
b3=Button(f1,text='OK',width=20)
#Additing it to root Window with value Y and side right and pad x
b3.place(x=200,y=250)
#display window using mainloop
root.mainloop()