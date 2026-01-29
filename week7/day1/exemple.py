import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Eden', 'Raphael'],
    'Age': [28, 34, 29, 32, None, 30],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Paris', None]
}
# print(df.head())
# ages = df['Age']
# print(df.sort_values(by='Age'))
# print(df.groupby('City')['Age'].mean())

### 1 creer et observer :
df = pd.DataFrame(data)
# print(df)
# names = df['Name']
# print(names)
# print(df['Age'].describe())
# age_max=df['Age'].max()
# vieille = df[df['Age']==age_max]
# print(f'age max est :{age_max} et le nom de la vielle est {vieille["Name"].values[0]} et elle habite a {vieille["City"].values[0]}')
# print(vieille)
# print(df.loc[1,'Age'])
# print(df.tail())
# print(df.iloc[5, 2])
# print(df['City'].value_counts())
# print(df.dropna())
# print(df.drop_duplicates())






# data = {
#     'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
#     'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
#     'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
#     'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
#     'Copies Sold': [500, 600, 800, 300, 450]
# }
#
# df = pd.DataFrame(data)
# # print(df)
# # print(df.describe())
# # print(df.info())
# # print(df.sort_values('Price'))
# # print(df[df['Genre']=='Classic'])
# print(df.groupby('Author')['Copies Sold'].sum())