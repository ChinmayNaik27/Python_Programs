
#import pymysql
import pymysql as mysql
#connect my sql data base to python
con=mysql.connect(host="localhost",user="root",password="root",database="abc")
#obtain cursor object
mycursor=con.cursor()
#exectueing sql query by using cursor object
sql="insert into dummy values('6','qmlmbg')"
mycursor.execute(sql)
con.commit()
con.close()
