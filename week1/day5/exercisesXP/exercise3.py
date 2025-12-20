# Exercise 3: Zara

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

clients = ", ".join(brand["type_of_clothes"][:-1]) + " and " + brand["type_of_clothes"][-1]
print(f"Zara's clients are looking for clothes for {clients}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(f"The last international competitor is: {brand['international_competitors'][-1]}")

print(f"Major colors in the US: {', '.join(brand['major_color']['US'])}")

print(f"Number of keys in the dictionary: {len(brand)}")

print(f"Keys: {list(brand.keys())}")


more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print("\n--- Result after merge ---")
print(f"New number of stores: {brand['number_stores']}")
print(f"Creation date restored: {brand['creation_date']}")
print(brand)