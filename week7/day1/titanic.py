import pandas as pd

# df = pd.read_csv("Titanic-Dataset.csv")
# print(df.head())
# femmes3=df[df['Pclass']==3]
# # print(femmes3)
# fe_life = femmes3[femmes3["Survived"]==1]
# print(len(fe_life))
# survivants_3e = len(df[(df['Pclass'] == 3) & (df['Survived'] == 1)])
# print(f"Nombre de survivants en 3ème classe : {survivants_3e}")
#
# mortes_f_2 = df[(df["Sex"] == 'female') & (df["Pclass"] == 2) & (df['Survived'] == 0)]
# print(mortes_f_2)
#
# femmes_mortes_2e = len(df[
#     (df['Sex'] == 'female') &
#     (df['Pclass'] == 2) &
#     (df['Survived'] == 0)
# ])
# print(f"Femmes de 2ème classe décédées : {femmes_mortes_2e}")

# print(df.groupby('Survived')['Age'].mean())
# prix_mx =df["Fare"].max()
# print(prix_mx)
# riche =df[df['Fare'] == prix_mx]
# print(riche)
# print(riche[['Name', 'Survived']]
#
# manquants = df['Age'].isnull().sum()
# print(f"\nNombre d'âges manquants : {manquants}")

# On recharge le fichier original
df_complet = pd.read_csv('Titanic-Dataset.csv')

# TABLEAU 1 : Les informations personnelles (on garde PassengerId pour la jointure)
df_perso = df_complet[['PassengerId', 'Name', 'Sex', 'Age']].copy()

# TABLEAU 2 : Les informations du voyage (Ticket, Prix, Survie, Classe)
# On ne garde que PassengerId et les colonnes "techniques"
df_voyage = df_complet[['PassengerId', 'Pclass', 'Fare', 'Survived']].copy()

# print("Tableaux créés avec succès !")

df_final = pd.merge(df_perso, df_voyage, on="PassengerId")
# print(df_final)

# pivot = df_final.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean')
# print("\n--- Taux de survie par classe et sexe ---")
# print(pivot)

df_final['Date_Achat'] = pd.to_datetime('2026-01-28') # Date fictive
df_final['Mois_Achat'] = df_final['Date_Achat'].dt.month
print("\n--- Extraction du mois réussie ---")
print(df_final[['Name', 'Date_Achat', 'Mois_Achat']].head())
