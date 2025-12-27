class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        current_letter ="A"
        sorted_animals ={}
        for animal in self.animals:
            if animal[0] == current_letter and current_letter not in sorted_animals:
                sorted_animals[current_letter]=[animal]
            elif animal[0] == current_letter and current_letter in sorted_animals:
                sorted_animals[current_letter].append(animal)
            else:
                current_letter = animal[0]
                sorted_animals[current_letter] = [animal]
        return sorted_animals

    def get_groups(self):
        for letter, lst in self.sort_animals().items():
            print(f"{letter}: {lst}")



brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")

brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
