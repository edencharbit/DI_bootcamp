# Exercise 2: Cinemax #2


family = {}
print("Enter the family members (enter 'quit' to end")
name = input("Member's name: ")
while name != 'quit':
    age = int(input(f"{name}'s age: "))
    family[name] = age
    name = input("Member's name: ")

ticket_price = 0
total_cost = 0
for member in family:
    if family[member] < 3 :
        ticket_price = 0
        print(f"The ticket price for {member} is ${ticket_price} because {member} is under 3 years old ")
    elif 12>=family[member]>=3:
        ticket_price = 10
        print(f"The ticket price for {member} is ${ticket_price} because {member} is 3 to 12 years old ")
        total_cost+=ticket_price
    else:
        ticket_price = 15
        print(
        f"The ticket price for {member} is ${ticket_price} because {member} is over 12 years old ")
        total_cost += ticket_price

print(f"The total cost is ${total_cost}")

