class A:
    def insert(self,id,name):
        self.sql = "insert into dummy values(%s,%s)"
        self.values=(id,name)
        mycursor.execute(self.sql,self.values)

    def select(self):
        self.sql = "select * from dummy"
        mycursor.execute(self.sql)

    def delete(self,id):
        self.sql = "delete from dummy where id =%s"
        self.values=(id)
        mycursor.execute(self.sql,self.values)

    def update(self,id,name):
        self.sql = "update dummy set name =%s where id = %s"
        self.values=(name,id)
        mycursor.execute(self.sql,self.values)
#Assigning Object
ob=A()
#importing Libraries
import pymysql as m
#connecting database
con=m.connect(host='localhost',user='root',password='root',database='abc')
#Creating Cursor objects
mycursor=con.cursor()
while True:
    x=int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update\nEnter no(Type any number to exit):"))
    if x==1:
        id = input("Enter id:")
        name = input("Enter name:")
        ob.insert(id,name)
    elif x==2:
        ob.select()
        x1=mycursor.fetchall()
        for z1 in x1:
            print(z1[0],z1[1])
    elif x==3:
        id = input("Enter id:")
        ob.delete(id)
    elif x==4:
        id = input("Enter id:")
        name = input("Enter name:")
        ob.update(id,name)
    z=input("Enter y to continue and n to exit:")
    if z!='y':
        break
con.commit()
con.close()