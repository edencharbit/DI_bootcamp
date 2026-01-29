# Exercise 8: Pizza Toppings

topping_lst =[]
topping = input("Choose a topping you want on your pizza: ")
while topping != 'quit':
    print(f"Adding {topping} to your pizza.")
    topping_lst.append(topping)
    topping = input("Choose a topping you want on your pizza: ")

pizza_cost = 10 + len(topping_lst)*2.50
print(f"You added the topping: {topping_lst} on your pizza, the total cost "
      f"of the pizza is : ${int(pizza_cost) if pizza_cost.is_integer() else pizza_cost}")
