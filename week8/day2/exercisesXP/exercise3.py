# Exercise 3: Visualizing Monthly Sales with a Bar Chart

import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May']
sales =[5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(10,6))
plt.bar(month, sales, color='skyblue', edgecolor='navy')
plt.xlabel('Month', fontweight='bold')
plt.ylabel('Sales Amount ($)', fontweight='bold')
plt.title('Monthly Sales Performance', fontsize=14)

for i, v in enumerate(sales):
    plt.text(i, v + 100, f"${v}", ha='center', fontweight='bold')

plt.show()