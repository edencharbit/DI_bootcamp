class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Step 1: Create cat objects
cat1 = Cat("Jerry", 3)
cat2 = Cat("Milou", 8)
cat3 = Cat("Tommy", 5)


# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest


# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(
    f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
