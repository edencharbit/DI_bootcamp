# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_output = {}
for i, key in enumerate(keys):
    val = values[i]
    dict_output[key] = val
print(dict_output)