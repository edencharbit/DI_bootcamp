# Exercise 2 : Creating a Line Plot for Temperature Variation

import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temp = [72, 74, 76, 80, 82, 78, 75]

plt.figure(figsize=(10,6))
plt.plot(days, temp, marker='o', linestyle='-', color='b')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperatures through the week')
plt.show()
