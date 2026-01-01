import string
import random

possible_comb = string.ascii_letters
random_str =""

for i in range(5):
    random_char = random.choice(possible_comb)
    random_str +=random_char

print(random_str)