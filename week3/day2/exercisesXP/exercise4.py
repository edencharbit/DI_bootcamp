# Exercise 4: Family and Person Classes


class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self, first_name):
        is_in_family = False
        for person in self.members:
            if person.first_name == first_name:
                is_in_family = True
                if person.is_18():
                    print(f"You are over 18 {first_name}, your parents Jane and John "
                          "accept that you will go out with your friends ")
                else:
                    print(f"Sorry {first_name}, you are not allowed to go out with your "
                          "friends.")
                break
        if is_in_family is False:
            print(f"{first_name} is not in the family")

    def family_presentation(self):
        print(f"The family name if {self.last_name}")
        print('The members of the family are : \n')
        for person in self.members:
            print(f"{person.first_name} is {person.age} years old")


person1 = Person('Lala', 26, "Charbit")


family_chabit = Family('Charbit')
family_chabit.born('Eden', 26)
family_chabit.born("Raph", 26)
family_chabit.born("Ariel", 1)
family_chabit.check_majority('Lala')
family_chabit.check_majority('Ariel')

# for member in family_chabit.members:
#     print(member.first_name)
#     family_chabit.check_majority(member.first_name)

family_chabit.family_presentation()



