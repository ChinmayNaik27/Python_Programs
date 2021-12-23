#importing library
import pymysql as m
class A:
    def __init__(self):
        self.con=m.connect(host='localhost',user='root',password='root',database='abc')
        self.mycursor=self.con.cursor()

    def insert(self,id,name):
        self.id=id
        self.name=name
        sql="insert into dummy values(%s,%s)"
        values=(id,name)
        self.mycursor.execute(sql,values)
        self.con.commit()
    def select(self):
        sql="select * from dummy"
        x=self.mycursor.fetchall()
        for i in x:
            print(i[0],i[1])
        self.mycursor.execute(sql)
    def delete(self,id):
        self.id=id
        sql="delete from dummy where id =%s"
        values=(self.id)
        self.mycursor.execute(sql,values)
        self.con.commit()
    def update(self,id,name):
        self.id=id
        self.name=name
        sql="update dummy set name=%s where id =%s"
        values=(self.name,self.id)
        self.mycursor.execute(sql,values)
        self.con.commit()
    def close(self):
        self.con.close()