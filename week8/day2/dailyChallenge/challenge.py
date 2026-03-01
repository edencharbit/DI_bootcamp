import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019.csv')
df_2019 = df.dropna()
plt.figure(figsize=(10,6))
plt.scatter(df_2019['Social support'], df_2019["Score"])
plt.title('Relationship between Social Support and Happiness Score (2019)')
plt.xlabel('Social Support')
plt.ylabel('Happiness Score')
plt.show()

regional_data = df_2019.groupby('Country or region')[['GDP per capita', 'Healthy life expectancy']].mean().sort_values(by='GDP per capita')
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,6))

ax1.bar(regional_data.index, regional_data['GDP per capita'], color='skyblue', alpha=0.7, label='GDP per Capita')
ax1.set_xlabel('Country or region')
ax1.set_ylabel('GDP per Capita ($)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2.plot(regional_data.index, regional_data['Healthy life expectancy'], color='red', marker='o', linewidth=2, label='Life Expectancy')
ax2.set_ylabel('Healthy Life Expectancy (Years)', color='red')
ax2.set_xlabel('Country or region')
ax2.tick_params(axis='y', labelcolor='red')


plt.title('Comparison of Economic Strength (GDP) and Health Outcomes by Region')
# fig.tight_layout()
plt.show()