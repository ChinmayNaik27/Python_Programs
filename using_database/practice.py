import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='abc')
coursor=con.cursor()
sql="insert into dummy values(6,'bahu'),(7,'kap'),(8,'xhvuyvd'),(9,' mncj'),(10,'qvgvd')"
coursor.execute(sql)
sql2="select id,name from dummy"
coursor.execute(sql2)
x=coursor.fetchall()
print(x)
for q in x:
    print(q[0],q[1])
con.commit()
con.close()