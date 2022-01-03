#Layout Grid
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
b1=Button(f1,text='OK')
#giving grid Postions
b1.grid(row=0,column=0)
b2=Button(f1,text='PS')
#Giving Grid Position
b2.grid(row=0,column=1)
b3=Button(f1,text='OK1')
#giving Grid Positions
b3.grid(row=1,column=0,columnspan=2,sticky=E+W)
b1=Button(f1,text='OK2')
#giving Grid positions
b1.grid(row=2,column=0,rowspan=2,stick=N+S)
#display window using mainloop
root.mainloop()