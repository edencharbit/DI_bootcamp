# Exercise 5: Let’s Create Some Personalized Shirts!

"""
Goal: Create a function to describe a shirt’s size and message,
with default values.
"""


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")


make_shirt()
make_shirt("medium")
make_shirt("small", "Python is not easy")