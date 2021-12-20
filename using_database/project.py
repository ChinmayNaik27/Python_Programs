



import pymysql as m

con=m.connect(host='localhost',user='root',password='root',database='abc')
mycoursor=con.cursor()
sql="insert into dummy values(100,'lab')"
mycoursor.execute(sql)
con.commit()
con.close()