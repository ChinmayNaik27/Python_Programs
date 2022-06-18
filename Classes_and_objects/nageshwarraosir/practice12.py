import pandas as pd
df1=pd.read_excel('D:/demo1.xlsx','Sheet1')
print(df1)
df2=pd.read_csv("D:\\demo1.csv")
print(df2)
empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
           "ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna", "Anant Nag"],
           "sal": [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99],
           "doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000", "9-9-1999"]}
print(empdata)