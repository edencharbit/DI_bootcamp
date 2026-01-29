# Exercise 8: What’s your name?

my_name = "Eden"
your_name = input("What is your name? ")

if my_name.lower()==your_name.lower():
    print("No way ! We have the same name! It's so funny, how parents have "
          "the same tastes ;)")
else:
    print(f"Nice to meet you {your_name.capitalize()}, my name is cooler, but yours cool "
          f"too :)")
