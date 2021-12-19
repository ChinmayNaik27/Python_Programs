# import pymysql as m
# con=m.connect(host='localhost',user='root',password='root',database='abc')
# mycoursor=con.cursor()
# sql="insert into dummy values('5','abcghy')"
# mycoursor.execute(sql)
# con.commit()
# con.close()
import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='test20')
mycoursor=con.cursor()
sql="insert into dummy values('2','Dimple','94217777569','dimple@gmail.com','r'),('3','Mary','2421777689','mary@gmail.com','z')"
mycoursor.execute(sql)
con.commit()
con.close()