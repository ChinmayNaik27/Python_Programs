
#import pymysql
import pymysql as mysql
#connect my sql data base to python
con=mysql.connect(host="localhost",user="root",password="root",database="abc")
#obtain cursor object
mycursor=con.cursor()
#exectueing sql query by using cursor object
sql="update dummy set name='bag' where id ='5'"
mycursor.execute(sql)
con.commit()
con.close()