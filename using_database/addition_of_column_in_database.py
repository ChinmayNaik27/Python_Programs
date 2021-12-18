import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='abc')
mycoursor=con.cursor()
sql="alter table dummy add phone varchar(55)"
mycoursor.execute(sql)
con.commit()
con.close()