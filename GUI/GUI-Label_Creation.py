#WAP for Label Creation in GUI
#impoting Module for gui
from tkinter import *
#creating root Object
root=Tk()
#set title
root.title("This is for Label Creation")
#setting Size
root.geometry("500x500")
#creating Frame Object
f1=Frame(root,bg="SkyBlue",width=500,height=500)
#adding frame to root window by calling pack
f1.pack(fill='both',expand=True)
#addinging Label to frame window
l1=Label(f1,text="Result is here",font=("Times New Roman",25,"italic"),bg="violet")
#adding Label to root window
l1.pack()
#display window using main loop
root.mainloop()
