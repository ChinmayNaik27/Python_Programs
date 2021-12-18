# import pymysql as m
# con=m.connect(host='localhost',user='root',password='root',database='abc')
# mycoursor=con.cursor()
# sql="insert into dummy values('5','abcghy')"
# mycoursor.execute(sql)
# con.commit()
# con.close()
import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='abc')
mycoursor=con.cursor()
sql="alter table dummy add gender varchar(55)"
mycoursor.execute(sql)
con.commit()
con.close()