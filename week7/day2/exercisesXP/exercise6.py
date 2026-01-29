import pandas as pd

df_sleep = pd.read_csv('Time Americans Spend Sleeping.csv')

print("First 5 rows of the Sleep Dataset:")
print(df_sleep.head())

print("\nDataset Information:")
df_sleep.info()