#WAP To Fetch all Records:
#importing libraries
import pymysql as m
#Establishing Connection
con=m.connect(host='localhost',user='root',password='root',database='abc')
#Creating Coursor Object
cour=con.cursor()
#executing Query
sql="select * from dummy"
cour.execute(sql)
#Fetching output
x=cour.fetchall()
print(x)
for all in x :
    print(all[0],all[1])