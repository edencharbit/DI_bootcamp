class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")


davids_dog = Dog("Lulu", 12)
sarahs_dog = Dog("Lala", 20)

print(f"David's dog: {davids_dog.name}, Height: {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: {sarahs_dog.name}, Height: {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The winner is {davids_dog.name}!")
elif sarahs_dog.height > davids_dog.height:
    print(f"The winner is {sarahs_dog.name}!")
else:
    print("Both dogs are the same height!")