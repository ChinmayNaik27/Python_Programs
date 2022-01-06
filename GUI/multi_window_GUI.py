#WAP for multiple windows in gui
from tkinter import *
class Login:
    def __init__(self,root):
        self.root=root
        self.f1=Frame(self.root,bg="skyblue",width=500,height=500)
        self.f1.pack(fill=BOTH,expand=True)
        self.e1 = Entry(self.f1, text="Enter Name", width=25)
        self.e1.place(x=300,y=350)
        self.e2 = Entry(self.f1, text="Enter Password:", width=25)
        self.e2.place(x=300,y=400)
        self.b1=Button(self.f1,text="Login")
        self.b1.grid(row=0,column=0)
        self.b2=Button(self.f1,text="Register",width=20,command=self.button_click)
        self.b2.grid(row=0,column=1)
    def button_click(self):
        self.f1.destroy()
        ob=Register(self.root)
class Register:
    def __init__(self,root):
        self.root=root
        self.f1=Frame(self.root,bg="Violet",width=500,height=500)
        self.f1.pack(fill=BOTH,expand=True)
        self.e1=Entry(self.f1,text="Enter Name",width=25)
        self.e1.pack()
        self.e2=Entry(self.f1,text="Enter Password:",width=25)
        self.e2.pack()
        self.b1=Button(self.f1,text="Register",width=20,command=self.button_click)
        self.b1.pack()
    def button_click(self):
        self.f1.destroy()
        ob2=Login(self.root)
root=Tk()
root.title("This is one Frame")
root.title("This is MultiWindow")
root.geometry("500x500")
ob1=Login(root)
root.mainloop()