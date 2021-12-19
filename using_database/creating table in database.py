import pymysql as m
con=m.connect(host='localhost',user='root',password='root',database='test20')
mycoursor=con.cursor()
# sql1="insert into dummy values ('1','Raghav','9421777689','raghavdutt@gmail.com'), ('2','Mary','2421777689','mary@gmail.com')"
sql2="select * from dummy limit 3,2"
# mycoursor.execute(sql)
mycoursor.execute(sql2)
#  mycoursor.execute(sql2)
con.commit()
con.close()