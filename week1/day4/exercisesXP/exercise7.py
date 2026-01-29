# Exercise 7: Favorite Fruits

fav_fruits = input("Enter your favorite fruits (separated by spaces):")
fav_lst = fav_fruits.split()
print(fav_lst)
chosen_fruit = input("Input the name of any fruit: ")
if chosen_fruit in fav_lst:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")