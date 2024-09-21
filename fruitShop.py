#11.	Fruit Shop
# Read the fruit name from user input
fruit = input("Enter the fruit: ")

# Read the day from user input
day = input("Enter the day: ")

# Read the quantity from user input and convert it to a float
quantity = float(input("Enter the quantity: "))

# Define the fruit prices for weekdays
weekday_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

# Define the fruit prices for weekends
weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

# Check if the day is valid and assign appropriate prices
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    fruits = weekday_prices
elif day in ["Saturday", "Sunday"]:
    fruits = weekend_prices
else:
    print("error")
    exit()  # Exit the program if the day is invalid

# Get the price of the fruit, if it exists
price = fruits.get(fruit)

# If the fruit does not exist, print an error
if price is None:
    print("error")
else:
    # Calculate and print the total price rounded to two decimal places
    print(f"{quantity * price:.2f}")

