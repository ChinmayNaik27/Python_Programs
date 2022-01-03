#layout Manager pack()
from tkinter import *
#creating root window
root=Tk()
#setting Title
root.title("This is frame ")
#change size
root.geometry("500x500")
#Frame Window
f1=Frame(root,bg="Orange",width=20,height=500)
#Additing it to root Window with value both
f1.pack(fill=BOTH,expand=True)
#Creating Label
l1=Label(f1,text='Result',font=('Times New Roman',20,'bold'),bg='yellow')
l1.pack()
b1=Button(f1,text='OK',width=20)
#Additing it to root Window with value X
b1.pack(fill=X)
b2=Button(f1,text='ppp',width=20)
#Additing it to root Window with value Y and side left and pad x
b2.pack(fill=Y,padx=240,side=LEFT)
b3=Button(f1,text='OK',width=20)
#Additing it to root Window with value Y and side right and pad x
b3.pack(fill=X,pady=200,side=RIGHT)
#display window using mainloop
root.mainloop()