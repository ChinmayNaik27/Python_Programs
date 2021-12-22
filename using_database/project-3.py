def insert(x1,y1):
    sql="insert into dummy values(%s,%s)"
    values=(x1,y1)
    mycursor.execute(sql,values)
def select():
    sql = "select * from dummy"
    mycursor.execute(sql)
def delete(x1):
    sql = "delete from dummy where name =%s"
    values=(x1)
    mycursor.execute(sql,values)
def update(y1,x1):
    sql = "update dummy set name =%s where id = %s"
    values = (y1,x1)
    mycursor.execute(sql, values)
def truncate():
    sql="truncate table dummy"
    mycursor.execute(sql)

#importing library
import pymysql as m
#connecting to mysql database
con=m.connect(host='localhost',user='root',password='root',database='abc')
#creating cursor object
mycursor=con.cursor()
while True:
    x=int(input("Following are no of opertions\n1.For Insert\n2.For select\n3.For Delete\n4.For update"
                "\n5.To Clear Complete Data inside table\nAnd any number to exit the proram:"))
    x1=input("Enter id:")
    y1=input("Enter name :")
    if x==1:
        insert(x1, y1)
        print("Insertion of Data is Successful!!!")
    elif x==2:
        print("Complete data is :")
        select()
        w1=mycursor.fetchall()
        for z1 in w1:
            print(z1[0],z1[1])
    elif x==3:
        delete(x1)
        print("Record Deleted successfully!!!")
    elif x==4:
        update(y1, x1)
        print("Data updated Successfully!!!")
    elif x==5:
        truncate()
        print("Table Cleared Successfully!!!")
    else:
        print("program closed successfully!!!")
        break
    z=input("Do You want to continue(y/n):")
    if z!='y':
        break
con.commit()
con.close()