#program Spinbox
#importing Libraries
from tkinter import *

def command1():
    s1=v1.get()
    s2=v2.get()
    l1['text']=str(s1)+" "+s2
#creating root Window
root=Tk()
#setting title
root.title("This is a Frame Window")
#changing window Size
root.geometry("500x500")
#creating Frame Window
f1=Frame(root,bg="violet",width=500,height=500)
#adding Frame Window to root Window
f1.pack(fill='both',expand=True)
#creating Label
l1=Label(f1,text="output",font=("arial",14,"underline"),bg="pink")
#adding label to root Window
l1.pack()
#Creating Spinbox
v1=IntVar()
sp1=Spinbox(f1,from_=0,to=10,textvariable=v1)
sp1.pack()                                        #adding spin button to frame
v2=StringVar()
sp2=Spinbox(f1,values=('Marathi','Hindi','English','Telgu'),textvariable=v2)
sp2.pack()                                         #adding spin button to frame
#Creating button
b1=Button(f1,text="OK",width=20,command=command1)
#adding button to root Window
b1.pack()
#display Window Using Mainloop
root.mainloop()