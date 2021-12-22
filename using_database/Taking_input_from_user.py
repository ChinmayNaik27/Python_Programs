#take values from user for input of data
#importing library
import pymysql as m
#conncting to database
abc=m.connect(host='localhost',user='root',password='root',database='abc')
#creating coursor object
mycursor=abc.cursor()
#executing queries
x=int(input("Enter the id :"))
s1=input("Enter name:")
sql="insert into dummy values( %s ,%s)"
values=(x,s1)
mycursor.execute(sql,values)
abc.commit()
abc.close()