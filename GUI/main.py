# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#WAP to take input From user
#importing Libraries
from tkinter import *
def button1():
    user=e1.get()
    passwd=e2.get()
    if user=='Chinmay' and passwd=='12345':
        l1['text']="Vaild User"
        l1['bg']="lightgreen"
    else:
        l1['text']="Invaild User"
        l1['bg']="red"
def button2():
    e1.delete(0,END)
    e2.delete(0,END)
#creating root window
root=Tk()
#set tittle
root.title("This is For Entry from user")
#Change size of window
root.geometry("500x500")
#Creating Frame Window
f1=Frame(root,bg="SkyBlue",width=500,height=500)
f1.pack(fill='both',expand=True)
#Taking Entry Form User
e1=Entry(f1,width=20)
e1.pack()            #adding it to root window
e2=Entry(f1,width=20,show='*')
e2.pack()            #adding it to root window
#addition of label
l1=Label(f1,text="Output",font=("Arial",14,'italic'),bg="Orange")
l1.pack()
#button Creation
b1=Button(f1,text="Login",width=20,command=button1)
b1.pack()
b2=Button(f1,text="Clear",width=20,command=button2)
b2.pack()
#display root window using mainloop
root.mainloop()