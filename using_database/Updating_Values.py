#take values from user for input of data
#importing library
import pymysql as m
#conncting to database
abc=m.connect(host='localhost',user='root',password='root',database='abc')
#creating coursor object
mycursor=abc.cursor()
#executing queries
x=input("Enter the id :")
s1=input("Enter name:")
sql="update dummy set name = %s where id = %s"
values=(s1,x)
mycursor.execute(sql,values)
abc.commit()
abc.close()
