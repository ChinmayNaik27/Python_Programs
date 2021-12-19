#importing module in sql moudle in python
import pymysql as m
#connecting database
con=m.connect(host='localhost',user='root',password='root',database='abc')
#mycourses enable queries
mycoursor=con.cursor()
#entering command in database
sql="alter table dummy add email varchar(55)"
#execute commands of database
mycoursor.execute(sql)
#saving commands in database
con.commit()
#connection disconnect database
con.close()
