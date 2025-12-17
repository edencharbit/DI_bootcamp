# Exercise 9: Cinemax Tickets

ages = input("Enter the age of each person in a family who wants to buy a "
             "movie ticket (separated by spaces): ")
lst_ages = [int(age) for age in ages.split()]
total_cost = 0
for age in lst_ages:
    if age < 3:
        total_cost += 0
    elif 12 >= age >= 3:
        total_cost += 10
    else:
        total_cost += 12
print(f"The total ticket cost for the family is: {total_cost}")

ages_input = input("Enter the ages of the teenagers (separated by spaces): ")
all_ages = [int(age) for age in ages_input.split()]
allowed_attendees = []

for age in all_ages:
    if 16 <= age <= 21:
        allowed_attendees.append(age)
    else:
        print(f"Access denied for age {age}: must be between 16 and 21.")

print("Final list of attendees (ages):", allowed_attendees)