import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#========== DATA PREPARATION =========
data = np.random.uniform(low=-5, high=35, size=(10, 12))

months = ["'Jan", "Feb", "Mar", "Apr", "May", "June", "Jul","Aug", "Sept", "Oct", "Nov", "Dec"]
cities = []
for i in range(10):
    cities.append(f"City_{i+1}")

df_temp = pd.DataFrame(data, cities, months)

print(df_temp)

# ========== DATA ANALYSIS ==========
aver_year = df_temp.mean(axis=1)
print(aver_year)

hot_city = aver_year.idxmax()
cold_city = aver_year.idxmin()
print(f"The city with hot temperatures is {hot_city} with an average of {aver_year[hot_city]}")
print(f"The city with cold temperatures is {cold_city} with an average of {aver_year[cold_city]}")


# ========== DATA VISUALIZATION ==========
df_temp.T.plot(figsize=(10,6), marker='o')
plt.title("Monthly Temperature Trends for Each City")
plt.ylabel("Temperature (°C)")
plt.xlabel("Month")
plt.xticks(ticks=range(len(df_temp.columns)), labels=df_temp.columns)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
