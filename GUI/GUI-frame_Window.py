#WAp to create a frame window in gui
#importing Libraries
from tkinter import *
#creating Root Object
root=Tk()
#setting Tittle
root.title("This is a Frame Window !")
#changing Window Size
root.geometry('500x500')
#creating Frame Object
f1=Frame(root,bg="skyblue",width=500,height=500)
#adding frame window to root
f1.pack()
#displaying root window by using main-loop
root.mainloop()