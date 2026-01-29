import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Iris.csv')
print(df.head())

mean_val = df['SepalLengthCm'].mean()
median_val = df['SepalLengthCm'].median()
mode_val = df['SepalLengthCm'].mode()[0]

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Mode: {mode_val:.2f}")


plt.hist(df['SepalLengthCm'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

plt.show()