#pandas
import pandas as pd
df=pd.read_excel("D:\\demo1.xlsx","Sheet1")
print(df)
import matplotlib.pyplot as plt
slices=[50,20,20,15]
dept=['Mkt','HR','Sales','Tech']
cols=['orange','yellow','cyan','pink']
plt.pie(slices,labels=dept,colors=cols,startangle=90,explode=(0.3,0,0,0.3),shadow=True,autopct='%.1f%%')
plt.title("Pie chart")
plt.legend()
plt.show()
