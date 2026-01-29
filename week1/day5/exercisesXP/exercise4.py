# Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict1 ={}
dict2={}
for i, char in enumerate(users):
    dict1[char] = i
    dict2[i] = char
dict3 = {}
users.sort()
for j, c in enumerate(users):
    dict3[c] = j
print(dict1)
print(dict2)
print(dict3)

