# Challenge 1: Sorting

string_to_sort = input("Enter words (separate the words with commas): ")
lst_str = string_to_sort.split(',')
lst_str.sort()
sorted_str = ','.join(lst_str)
print(sorted_str)
