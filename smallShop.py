# 5.	Small Shop
# Get product, city, and quantity input from the user
product = input("Enter the product: ")
city = input("Enter the city: ")
quantity = float(input("Enter the quantity: "))

# Check if the city is "London"
if city == "London":
    # Prices in London
    if product == "coffee":
        print(f"{0.50 * quantity:.2f}")
    elif product == "water":
        print(f"{0.80 * quantity:.2f}")
    elif product == "beer":
        print(f"{1.20 * quantity:.2f}")
    elif product == "sweets":
        print(f"{1.45 * quantity:.2f}")
    elif product == "peanuts":
        print(f"{1.60 * quantity:.2f}")

# Check if the city is "Rome"
elif city == "Rome":
    # Prices in Rome
    if product == "coffee":
        print(f"{0.40 * quantity:.2f}")
    elif product == "water":
        print(f"{0.70 * quantity:.2f}")
    elif product == "beer":
        print(f"{1.15 * quantity:.2f}")
    elif product == "sweets":
        print(f"{1.30 * quantity:.2f}")
    elif product == "peanuts":
        print(f"{1.50 * quantity:.2f}")

# Check if the city is "Paris"
elif city == "Paris":
    # Prices in Paris
    if product == "coffee":
        print(f"{0.45 * quantity:.2f}")
    elif product == "water":
        print(f"{0.70 * quantity:.2f}")
    elif product == "beer":
        print(f"{1.10 * quantity:.2f}")
    elif product == "sweets":
        print(f"{1.35 * quantity:.2f}")
    elif product == "peanuts":
        print(f"{1.55 * quantity:.2f}")




