# Challenge 1: Letter Index Dictionary

user_word = input("Enter a word: ")
dict_word = {}
for index, char in enumerate(user_word):
    if char in dict_word:
        dict_word[char].append(index)
    else:
        dict_word[char] = [index]

print(dict_word)
