# Exercise 1 : Convert lists to dictionary


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Combine the two lists into a dictionary
dictionary = dict(zip(keys, values))

# Display the result
print(dictionary)






# Exercise 2 : Cinemax

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Start with a total of 0
total = 0

# Loop through the dictionary
for name, age in family.items():
    if age < 3:
        ticket = 0
    elif 3 <= age <= 12:
        ticket = 10
    else:
        ticket = 15

    # Add ticket price to total
    total += ticket
    print(f"{name} is {age} years old, ticket price: {ticket}$")

# Display the total
print(f"Total price for the family: {total}$")






#Exercise 3 : Zara

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

# Modify number_stores to 2
brand.update({"number_stores": 2})

# Print Zara's customers
print(f"Zara's customers are: {brand['type_of_clothes']}")

# Add country_creation key
brand["country_creation"] = "Spain"

# Check if international_competitors exists, then add Desigual
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete creation_date
brand.pop("creation_date")

# Print last competitor
print(f"Last competitor: {brand['international_competitors'][-1]}")

# Print major colors in the US
print(f"Major colors in the US: {brand['major_color']['US']}")

# Print number of keys
print(f"Number of keys: {len(brand.keys())}")

# Print all keys
print(f"All keys: {brand.keys()}")

# Merge with more_on_zara
more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print(f"Merged dictionary: {brand}")





# Exercise 4 : Function to describe a city and its country

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call the function with and without country
describe_city("Nantes", "France")
describe_city("New York")
describe_city("Abidjan", "Côte d'Ivoire")






# Exercise 5 : Random number

import random

def compare_numbers(number):
    # Generate one random number
    random_number = random.randint(1, 100)
    
    # Compare the two numbers
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")

# Call the function with a number
compare_numbers(50)
    






# Exercise 6 : Create a personalized t-shirt

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt("medium")

# Small shirt with custom message
make_shirt("small", "Hello World")

# Bonus : keyword arguments
make_shirt(size="small", text="Hello!")




# Exercise 7 : Temperature advice

import random

def get_random_temp():
    # Generate a random temperature between -10 and 40
    return random.randint(-10, 40)

def main():
    # Get and display the temperature
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    # Give advice based on temperature
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("Beautiful weather! Enjoy the day!")
    elif temp < 32:
        print("It's getting hot! Stay hydrated.")
    else:
        print("It's scorching! Stay cool.")

main()






# Exercise 8 : Pizza toppings

# Start with an empty list and base price
toppings = []
base_price = 10
topping_price = 2.50

# Ask for toppings until user types "quit"
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    
    if topping == "quit":
        break
    
    # Add topping to the list and display message
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Calculate total price
total = base_price + (len(toppings) * topping_price)

# Display final result
print(f"\nYour toppings: {toppings}")
print(f"Total price: {total}$")


