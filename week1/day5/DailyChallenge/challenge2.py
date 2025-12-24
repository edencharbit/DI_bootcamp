# Challenge 2: Affordable Items

items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000",
                  "PC": "$1200"}
wallet = "$1"
basket = []
updated_wallet = int(wallet[1:].replace(",", ""))
for item in items_purchase:
    price = int(items_purchase[item][1:].replace(",", ""))
    if price <= updated_wallet:
        basket.append(item)
        updated_wallet -= price
if len(basket) == 0:
    print("Nothing")
else:
    basket.sort()
    print(basket)
