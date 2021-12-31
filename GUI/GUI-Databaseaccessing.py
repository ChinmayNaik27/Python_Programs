#importig Libraries
from tkinter import *
import pymysql as mysql
#Creating Classes
class Database:
    def __init__(self):
        """
        Step1-connecting to sql
        Step2-Creating Cursor Object
        """
        self.con=mysql.connect(host='localhost',user='root',password='root',database='abc')
        self.mycursor=self.con.cursor()
    def insert(self,id1,name):
        """
        :param id1:To Take id as input
        :param name:  To take name as input
        :return: inserts the id and name in database after execution
        """
        self.id=id1
        self.name=name
        self.sql="insert into dummy values(%s,%s)"
        self.values=(id1,name)
        self.mycursor.execute(self.sql,self.values)
        self.con.commit()
    def update(self,id1,name):
        """
        :param id1:To Take id as input
        :param name:To take name as input
        :return:updates  name  in given id in database after execution
        """
        self.id=id1
        self.name=name
        self.sql="update dummy set name=%s where id=%s"
        self.values=(name,id1)
        self.mycursor.execute(self.sql,self.values)
        self.con.commit()
    def show(self,id1):
        """

        :param id1: selects id
        :return: Fetchs out record and displays output
        """
        self.id=id1
        self.sql="select * from dummy where id=%s"
        self.values=(self.id)
        self.mycursor.execute(self.sql,self.values)
        self.x=self.mycursor.fetchone()
        e2.insert(0,self.x[1])
    def close(self):
        """
        :return:closes Database
        """
        self.con.close()
#Assigning object to a class
ob=Database()
#functions
def data():
    id1=e1.get()
    name=e2.get()
    ob.insert(id1,name)
    l1['text']="Record Added"
def update():
    id1 = e1.get()
    name = e2.get()
    ob.update(id1, name)
    l1['text'] = "Record Updated"
def view():
    id1=e1.get()
    ob.show(id1)
    l1['text']="Record is viewed"
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
#creating root window
root=Tk()
#Setting title
root.title("This is for database updation")
#Changing the size of Window
root.geometry("500x500")
#creating frame window
f1=Frame(root,bg="SkyBlue",width=500,height=500)
#adding frame window to root window
f1.pack(fill='both',expand=True)
#creating Label
l1=Label(f1,text="Output",font=("Times New Roman",14,"italic"),bg="Violet")
#Adding label to root window
l1.pack()
#Creating Entry Box / text field for id
e1=Entry(f1,width=25)
#adding to frame window
e1.pack()
#Creating Text Field for name
e2=Entry(f1,width=25)
#Adding into frame Window
e2.pack()
#creating button for insert
b1=Button(f1,text="ADD",width=20,command=data)
#adding button to root window
b1.pack()
#creating Button for update
b2=Button(f1,text="UPDATE",width=20,command=update)
# adding button to root window
b2.pack()
#creating button for clear
b3=Button(f1,text="CLEAR",width=20,command=clear)
#adding button to root window
b3.pack()
#creating Button for viewing records
b4=Button(f1,text="VIEW",width=20,command=view)
# adding button to root window
b4.pack()
#display window using mainloop
root.mainloop()
#closing database
ob.close()