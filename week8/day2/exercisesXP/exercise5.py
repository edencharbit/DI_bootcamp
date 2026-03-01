# Exercise 5 : Data Visualisation Using MatPlotLib

import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = []
for val in x:
    y.append(val**2)

plt.figure(figsize=(10,6))
plt.plot(x, y, color='red', marker='o', label='$y = x^2$')
plt.title('Line Plot of $y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()


products = ['A', 'B', 'C', 'D']
sales = [15, 30, 45, 20]

plt.figure(figsize=(6, 4))
plt.bar(products, sales, color='teal')
plt.title('Weekly Sales of Products')
plt.xlabel('Product')
plt.ylabel('Sales Value')
plt.show()


fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
pourcentages = [40, 30, 20, 10]
couleurs = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

plt.figure(figsize=(6, 6))
plt.pie(pourcentages, labels=fruits, autopct='%1.1f%%', startangle=140, colors=couleurs)
plt.title('Favorite Fruits Distribution')
plt.legend(fruits, loc="upper right")
plt.show()