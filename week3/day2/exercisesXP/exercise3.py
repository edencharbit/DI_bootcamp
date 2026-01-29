# Exercise 3: Dogs Domesticated

import random
from week3.day2.exercisesXP.exercise2 import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ', '.join(args)
        print(f"{names} all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs",
                  "shakes your hand", "plays dead"]
        index = random.randint(0, len(tricks)-1)
        if self.trained is True:
            print(f'{self.name} {tricks[index]}')


my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
