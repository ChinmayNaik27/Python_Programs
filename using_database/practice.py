import pymysql as d
con=d.connect(host='localhost',user='root',password='root',database='abc')
mycourser=con.cursor()
sql="insert into dummy values('9','xcttysvf')"
mycourser.execute(sql)
con.commit()
con.close()