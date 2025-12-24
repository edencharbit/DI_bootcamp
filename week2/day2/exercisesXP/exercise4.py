# Exercise 4: Random

"""Goal: Create a function that generates random numbers and compares them."""

import random


def random_number(your_number):
    random_number = random.randint(1, 100)
    if your_number == random_number:
        print("Success")
    else:
        print(
            f"Fail! Your number: {your_number}, Random number: {random_number}"
        )

random_number(12)