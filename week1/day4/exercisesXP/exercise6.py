# Exercise 6: While Loop

user_name = input("Enter your name: ")
while user_name.isdigit() or len(user_name) < 3 or not user_name.istitle():
    user_name = input("Give the correct name: ")
else:
    print("thank you")
