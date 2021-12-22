class A:
    def insert(self,x,y):
        x=input("Enter id")
        y=input("Enter name:")
        self.sql = "insert into dummy values(%s,%s)"
        mycursor.execute(self.sql)

    def select(self,x,y):
        x=input("Enter id")
        y=input("Enter name:")
        self.sql = "select * from dummy"
        mycursor.execute(self.sql)

    def delete(self):
        self.sql = "delete from dummy where name ='hari'"
        mycursor.execute(self.sql)

    def update(self):
        self.sql = "update dummy set name ='hari' where id = 69"
        mycursor.execute(self.sql)
ob=A()
import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='abc')
mycursor=con.cursor()
x=int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update\nEnter no:"))
print("(Type any no to exit)")
while True:
    if x==1:
        ob.insert()
    elif x==2:
        ob.select()
        x1=mycursor.fetchall()
        for z1 in x1:
            print(z1[0],z1[1])
    elif x==3:
        ob.delete()
    elif x==4:
        ob.update()
    x=input("Enter y to continue and n to exit:")
    if x!='y':
        break
con.commit()
con.close()