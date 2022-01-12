# GUI based project database
from tkinter import *
import pymysql as m
class Login:

    def __init__(self,root):
        self.root=root
        self.f1=Frame(self.root,bg='Orange',width=500,height=500)
        self.f1.pack(fill=BOTH,expand=True)
        self.e1 = Entry(self.f1, width=20)
        self.e1.pack(pady=10)
        self.e2 = Entry(self.f1, width=20)
        self.e2.pack(pady=10)
        self.l1=Label(self.f1,text="Result",font=("Times New Roman",15,"bold"),bg="pink")
        self.l1.pack()
        self.b1=Button(self.f1,text="Login",width=20,command=self.button_click2)
        self.b1.pack(pady=10)
        self.b2 = Button(self.f1, text="Register", width=20, command=self.button_click)
        self.b2.pack(pady=10)
    def data1(self):
        self.con1 = m.connect(host="localhost", user="root", password="root", database="userlogin")
        self.cursor = self.con1.cursor()

    def button_click(self):
        self.f1.destroy()
        ob2=Register(self.root)
    def button_click2(self):
        self.user1 = self.e1.get()
        self.password = self.e2.get()
        self.data1()
        self.sql = "select * from table1"
        self.cursor.execute(self.sql)
        self.x = self.cursor.fetchone()
        if self.x[0] == self.user1 and self.x[1] == self.password:
            self.l1['text'] = "Login successful"
            self.l1['bg'] = "LightGreen"
            self.f1.destroy()
            ob3 = Database(self.root)
        else:
            self.l1['text'] = "Invalid User"
        self.con1.close()
class Database:
    def __init__(self,root):
        self.root = root
        self.con = m.connect(host="localhost", user="root", password="root", database="abc")
        self.cursor = self.con.cursor()
        self.f1 = Frame(self.root, bg='lightgreen', width=500, height=500)
        self.f1.pack(fill=BOTH, expand=True)
        self.e1 = Entry(self.f1, width=20)
        self.e1.pack(pady=10)
        self.e2 = Entry(self.f1, width=20)
        self.e2.pack(pady=10)
        self.l1 = Label(self.f1, text="Result", font=("Times New Roman", 25, "italic"), bg="pink")
        self.l1.pack()
        self.b1 = Button(self.f1, text="Insert", width=20, command=self.insert)
        self.b1.pack(pady=10)
        self.b2 = Button(self.f1, text="Update", width=20, command=self.update)
        self.b2.pack(pady=10)
        self.b3 = Button(self.f1, text="Delete", width=20, command=self.delete)
        self.b3.pack(pady=10)
        self.b4 = Button(self.f1, text="Close DB", width=20, command=self.close)
        self.b4.pack(pady=10)
    def insert(self):
        self.id = self.e1.get()
        self.name = self.e2.get()
        self.sql = "insert into dummy values(%s,%s)"
        self.values = (self.id, self.name)
        self.cursor.execute(self.sql, self.values)
        self.con.commit()
        self.l1['text']="Record Inserted Successfully"
    def update(self):
        self.id = self.e1.get()
        self.name = self.e2.get()
        self.sql = "update dummy set name=%s where id=%s"
        self.values = (self.name, self.id)
        self.cursor.execute(self.sql, self.values)
        self.l1['text'] = "Record Updated Successfully"
        self.con.commit()
    def delete(self):
        self.id = self.e1.get()
        self.sql = "delete from dummy where id=%s"
        self.values = (self.id)
        self.cursor.execute(self.sql, self.values)
        self.l1['text'] = "Record Deleted Successfully"
        self.con.commit()
    def close(self):
        self.con.close()
        self.f1.destroy()
        ob=Login(self.root)
class Register(Login):
    def __init__(self,root):
        self.root=root
        self.f1=Frame(self.root,bg='Violet',width=500,height=500)
        self.f1.pack(fill=BOTH,expand=True)
        self.e1=Entry(self.f1,width=20)
        self.e1.pack(pady=10)
        self.e2=Entry(self.f1,width=20)
        self.e2.pack(pady=10)
        self.b1=Button(self.f1,text="Register",width=20,command=self.button_click)
        self.b1.pack(pady=10)
        self.b2=Button(self.f1,text="Back",width=20,command=self.button_click1)
        self.b2.pack(pady=10)
        self.l1=Label(self.f1,text="",font=("Times New Roman",15,"italic"),bg="skyblue")
        self.l1.pack(pady=5)
    def button_click(self):
        self.user1 = self.e1.get()
        self.password = self.e2.get()
        self.data1()
        self.sql = "insert into table1 values(%s,%s)"
        self.values=(self.user1,self.password)
        self.cursor.execute(self.sql,self.values)
        self.con1.commit()
        self.l1['text']="Record Added"
        self.f1.destroy()
        ob2=Login(self.root)
    def button_click1(self):
        self.f1.destroy()
        ob2=Login(self.root)
root=Tk()
root.title("This is multi window")
root.geometry("500x500")
ob=Login(root)

root.mainloop()