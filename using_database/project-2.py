
import pymysql as m

class A:
    def __init__(self):
        ##connecting database
        self.con=m.connect(host='localhost',user='root',password='root',database='abc')
        #creating cursor object
        self.cursor=self.con.cursor()
    def insert(self,id,name):
        self.id=id
        self.name=name
        self.sql="insert into dummy values(%s,%s)"
        self.values=(id,name)
        self.cursor.execute(self.sql,self.values)
        self.con.commit()
    def update(self,id,name):
        self.id=id
        self.name=name
        self.sql="update dummy set name=%s where id=%s"
        self.values=(name,id)
        self.cursor.execute(self.sql,self.values)
        self.con.commit()
    def delete(self,id):
        self.id=id
        self.sql="delete from dummy where id =%s"
        self.values=(id)
        self.cursor.execute(self.sql,self.values)
        self.con.commit()
    def select(self):
        self.sql="select * from dummy"
        self.cursor.execute(self.sql)
        x11=self.cursor.fetchall()
        for i in x11:
            print(i)
    def truncate(self):
        self.sql="truncate table dummy"
        self.cursor.execute(self.sql)
    def close(self):
        self.con.close()
ob=A()
while True:
    x = int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update"
                  "\n5.To Clear Complete Data inside table\nAnd any number to exit the proram:"))
    if x==1:
        id = input("Enter id:")
        name = input("Enter name :")
        ob.insert(id,name)
        print("Record Inserted Successfully")
    elif x==2:
        print("Data is:")
        ob.select()
    elif x==3:
        id = input("Enter id:")
        ob.delete(id)
        print("Record Cleared Successfully")
    elif x==4:
        id = input("Enter id:")
        name= input("Enter name:")
        ob.update()
        print("Record Updated Successfully")
    elif x==5:
        ob.truncate()
        print("Table Cleared Successfully")
    else:
        break
    z2=input("Wish to Continue???(y/n):")
    if z2!='y':
        break