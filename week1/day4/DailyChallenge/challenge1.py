# Challenge 1: Multiples of a Number

num = int(input("enter a number: "))
length = int(input('enter a length: '))
lst_multiples =[]
for i in range(length):
    lst_multiples.append(num*(i+1))
print(lst_multiples)