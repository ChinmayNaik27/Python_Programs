#WAP to fetching some records
##imorting Library
import pymysql as m
#Connecting to database
xyz=m.connect(host='localhost',user='root',password='root',database='abc')
#Creating Coursor Object
cos=xyz.cursor()
#executing queries
sql="select * from dummy"
cos.execute(sql)
#fetching records
x=cos.fetchmany(2)                   #fetches 2 records
print(x)
for c1 in x:
    print(c1[0],c1[1])