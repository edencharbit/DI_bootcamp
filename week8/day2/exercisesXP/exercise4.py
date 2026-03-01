# Exercise 4 : Data Visualisation

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
total_quant = df['quantity'].sum()
print(f'the total quantity of products sold by the company is : {total_quant}')


category_revenue = df.groupby('category')['revenue'].sum()
highest_revenue_category = category_revenue.idxmax()
highest_revenue_value = category_revenue.max()
print(f'the category that had the highest revenue is {highest_revenue_category} '
      f'generated {highest_revenue_value}')

average_revenue_per_sale = df['revenue'].mean()
print(f"the average revenue per sale is {average_revenue_per_sale}")


df['date'] = pd.to_datetime(df['date'])
df['quarter'] = df['date'].dt.to_period('Q').astype(str)
quarterly_revenue = df.groupby('quarter')['revenue'].sum()
print(quarterly_revenue)

plt.figure(figsize=(10,6))
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']
plt.bar(quarterly_revenue.index, quarterly_revenue.values, color=colors)
plt.xlabel('Quarter')
plt.ylabel('Sales Amount ($)')
plt.title('Total Revenue Generated in Each Quarter')

for i, v in enumerate(quarterly_revenue.values):
    plt.text(i, v + 100, f"${v}", ha='center', fontweight='bold')
plt.show()


