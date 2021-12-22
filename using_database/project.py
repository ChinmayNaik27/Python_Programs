def insert():
    sql="insert into dummy values(%s,%s)"
    values=(x1,y1)
    mycursor.execute(sql,values)
def select():
    sql = "select * from dummy"
    mycursor.execute(sql)
def delete():
    sql = "delete from dummy where name =%s"
    values=(x1)
    mycursor.execute(sql,values)
def update():
    sql = "update dummy set name =%s where id = %s"
    values = (y1,x1)
    mycursor.execute(sql, values)

#importing library
import pymysql as m
#connecting to mysql database
con=m.connect(host='localhost',user='root',password='root',database='abc')
#creating cursor object
mycursor=con.cursor()
while True:
    x=int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update"
                "\nAnd any number to exit the proram:"))
    if x==1:
        x1=input("Enter id:")
        y1=input("Enter name :")
        insert()
    elif x==2:
        select()
        w1=mycursor.fetchall()
        for z1 in w1:
            print(z1[0],z1[1])
    elif x==3:
        x1=input("Enter id:")
        delete()
        print("Record Deleted successfully")
    elif x==4:
        y1 = input("Enter name:")
        x1 = input("Enter id:")
        update()
    else:
        print("program closed successfully")
        break
    z=input("Do You want to continue(y/n):")
    if z!='y':
        break

con.commit()
con.close()