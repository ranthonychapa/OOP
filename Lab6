import pandas as pd
df = pd.read_csv('data01.csv')
import matplotlib.pyplot as plt
#1) Find the median of the median_house_value column and print it
x = df['median_house_value'].median()
print('Median House Value:',x)
#2) Find the total rooms that are less than 500, then replace them with the median value of total_rooms
y = df['total_rooms'].median()
print('Total Room Median',y)
df.loc[df['total_rooms']<500, 'total_rooms'] = y
df.head(50)
#3) Print the housing_median_age less than 25, and print the rows
z = df.loc[df['housing_median_age']<25]
display(z)
#4) Draw any type of graph for any two relevant columns in the CSV file
df.plot(kind= 'line',x = 'total_rooms', y = 'total_bedrooms')
plt.show()

df.plot(kind = 'scatter', x = 'housing_median_age', y = 'median_house_value')
plt.show()


