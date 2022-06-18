import pandas as pd
#reading dat afrom csv file
df=pd.read_csv("D:\\demo1.csv")
print(df)
#reading data from excel file
df1=pd.read_excel("D:\\demo1.xlsx",'Sheet1')
print(df1)
#reading data from List of Tuples
empdata = [(1001, 'Ganesh Rao', 10000.00, '10-10-2000'), (1002, 'Anil Kumar', 23000.50, '3-20-2002'), (1003, 'Gaurav Gupta', 18000.33, '03-03-2002'),
           (1004, 'Hema Chandra', 16500.50, '10-09-2000'), (1005, 'Laxmi Prasanna', 12000.75, '08-10-2000'), (1006, 'Anant Nag', 9999.99, '09-09-1999')]
df2=pd.DataFrame(empdata,columns=['emp1','ename','sal','date'])
print(df2)
# reading data from dictionary
empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
               "ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna", "Anant Nag"],
               "sal": [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99],
               "doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000", "9-9-1999"]}
df3=pd.DataFrame(empdata)
# print(df3)
# print(df[::])
# print(df[::2])
# print(df[8:4:-2])
# print(df[8:4:-1])
# a1=df.columns
# print(a1)
# a2=df.size
# print(a2)
# print(df['sal'])
# print(df[['sal','eno']])
# print(df['sal'].max())
# print(df['sal'].min())
# df=[df.sal==df.sal.max()]
# print(df)
# df=[df.sal >10000]
# print(df)
# print(df.index)
# df1=df.loc[4]
# print(df1)
# df2=df.set_index('eno')
# print(df2)
# print(df2.loc[1003])
df=df.set_index('eno')
print(df)
print(df.sal<df.sal.mean())
e=df1.fillna({'ename':'No Name','doj':'22-12-2021','sal':'0'})
print(e)
f=df1.dropna()
print(f)
df2=df1.sort_values('doj')
print(df2)
# import matplotlib.pyplot as plt
# x=df1['eno']
# y=df1['sal']
# plt.bar(x,y)
# plt.title("This is a dummy Graph!!")
# plt.xlabel("employee number----->")
# plt.ylabel("Salary------->")
# plt.show()
#matplot lib
# import matplotlib.pyplot as plt
# x=df1['sal']
# y=df1['eno']
# plt.bar(y,x)
# plt.title("This is a batr graph!!!")
# plt.xlabel("ename----->")
# plt.ylabel("sal of employee----------->")
# plt.show()
#
import matplotlib.pyplot as plt
# print(df1.describe())
# print(df1[df1.sal>30000])
# print(df1[df1.sal==df1.sal.max()])
# print(df1[['doj', 'ename']][df.sal>10000])
# x=[1001,1003,1005,1007,1009,1011]
# y=[10000,23000.500,18000,16500.50,12000.56,9999.99]
# x1=[1002,1004,1006,1008,1010,1012]
# y1=[50000,2000.500,8000,16000.50,2000.56,9009.99]
# plt.bar(x,y,label='Sales')
# plt.bar(x1,y1,label='HR')
# plt.xlabel("eno")
# plt.ylabel("ESAL")
# plt.legend()
# plt.show()
# ex=[22,34,45,66,67,3,32,12,34,97,56,33,43]
# bins=[0,10,20,30,40,50,60]
# plt.hist(ex,bins,histtype='bar',rwidth=0.8,color='red')
# plt.xlabel("Eno")
# plt.ylabel("Sal")
# plt.title("Histogram")
# plt.show()
# slices=[50,20,20,15]
# dept=['Mkt','HR','Sales','Tech']
# cols=['Green','Yellow','Brown','Blue']
# plt.pie(slices,labels=dept,colors=cols)
# plt.title("Pie chart")
# plt.show()
# slices=[50,20,20,15]
# dept=['Mkt','HR','Sales','Tech']
# cols=['Green','grey','cyan','purple']
# plt.pie(slices,labels=dept,colors=cols,startangle=90)
# plt.title("Pie chart")
# plt.show()
# slices=[50,20,20,15]
# dept=['Mkt','HR','Sales','Tech']
# cols=['Green','orange','cyan','purple']
# plt.pie(slices,labels=dept,colors=cols,startangle=90,shadow=True)
# plt.title("Pie chart")
# plt.show()
# slices=[50,20,20,15]
# dept=['Mkt','HR','Sales','Tech']
# cols=['Green','orange','cyan','purple']
# plt.pie(slices,labels=dept,colors=cols,startangle=90,shadow=True,explode=(0,0.3,0,0))
# plt.title("Pie chart")
# plt.show()
slices=[50,20,20,15]
dept=['Mkt','HR','Sales','Tech']
cols=['Green','orange','cyan','purple']
plt.pie(slices,labels=dept,colors=cols,startangle=90,shadow=True,explode=(0,0,0,0.2),autopct='%.1f%%')
plt.title("Pie chart")
plt.show()