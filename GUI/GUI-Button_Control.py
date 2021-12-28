#WAP For GUI using Buttons
#importing Libraries
from tkinter import *
#Functions
def button1():
    l1['text']="RED"
    l1['bg'] = "Red"
def button2():
    l1['text']="GREEN"
    l1['bg'] = "Green"
#Creating Root Object
root=Tk()
#setting tittle
root.title("This is for Control using buttons")
#Changing window size
root.geometry("500x500")
#creating frame window
f1=Frame(root,bg="SkyBlue",width=500,height=500)
#adding frame window to root window
f1.pack(fill="both",expand=True)
#creating Label
l1=Label(f1,text="This is Result",font=("Times New Roman",14,"bold"),bg="Yellow")
#addition of label to root window
l1.pack()
#adding Button to frame window
b1=Button(f1,text="RED",width=20,command=button1)
b1.pack()
b2=Button(f1,text="Green",width=20,command=button2)
b2.pack()
#display root window using main-loop
root.mainloop()
