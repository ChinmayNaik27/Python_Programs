# to display profits of a company year-wise 
import matplotlib.pyplot as plt 
years = ['2012', '2013', '2014', '2015', '2016', '2017'] 
profits = [9, 10, 10.5, 8.8, 10.9, 9.75]
# create the line graph
plt.plot(years, profits, 'cyan')
# set title and labels 
plt.title('XYZ COMPANY') 
plt.xlabel('Years') 
plt.ylabel('Profits in Million Rs')
# show the line chart
plt.show()
