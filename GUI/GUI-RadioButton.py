#program for radio button
#importing libraries
from tkinter import *
def check():
    s1=""
    if v1.get()==1:
        s1="Male"
    elif v1.get()==2:
        s1="Female"
    l1['text']=s1
#creating root Window
root=Tk()
#setting tittle
root.title("This is a Frame window")
#Changing Size of Window
root.geometry("500x500")
#creating Frame Window
f1=Frame(root,bg="SkyBlue",width=500,height=500)
#adding Frame Window to root window
f1.pack(fill='both',expand=True)
#creating Label
l1=Label(f1,text="Result",font=("arial",15,"bold"),bg="Orange")
#addition of label to frame window
l1.pack()
#setting Radio_Button
v1=IntVar()
r1=Radiobutton(f1,text="Male",variable=v1,value=1)
#adding radio_button To The Frame window
r1.pack()
r2=Radiobutton(f1,text="Female",variable=v1,value=2)
#adding radio button to the frame window
r2.pack()
#Creating Button
b1=Button(f1,text="Ok",width=20,command=check)
#adding button to frame window
b1.pack()
#display window using mainloop
root.mainloop()