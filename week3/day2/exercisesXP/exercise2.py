# Exercise 2: Dogs

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        dog_winner = self.run_speed() * self.weight
        other_dog_winner = other_dog.run_speed() * other_dog.weight
        if dog_winner > other_dog_winner:
            return (f"{self.name} won the fight")
        elif other_dog_winner > dog_winner:
            return (f"{other_dog.name} won the fight")
        else:
            return ("It's a tie")


dog1 = Dog("Rex", 3, 67)
dog2 = Dog("Volt", 5, 23)
dog3 = Dog("Pilou", 10, 93)
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
