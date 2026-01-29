# Exercise 7: Faker Module

from faker import Faker

users = []


# 2. On crée la fonction demandée
def add_users(num):
    fake = Faker()  # C'est notre outil magique

    for _ in range(num):
        user_info = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user_info)


add_users(5)

print(users)