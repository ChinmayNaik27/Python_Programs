#Fetching one Record

#import library
import pymysql as m
#connecting to database
abc=m.connect(host='localhost',user='root',password='root',database='abc')
#Creating coursor objects
mycoursor=abc.cursor()
#executing Queries
sql="select * from dummy"
mycoursor.execute(sql)
#Fetching Records
x=mycoursor.fetchone()
print(x)
# Seperating Records
for a in x:
    print(a)