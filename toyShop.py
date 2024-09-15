#4.	Toy Shop
# Prices of the toys in USD
puzzle_price = 2.60  # Price of one puzzle
doll_price = 3.00  # Price of one talking doll
bear_price = 4.10  # Price of one teddy bear
minion_price = 8.20  # Price of one minion
truck_price = 2.00  # Price of one truck

# Input: Read the price of the trip and the number of each toy sold
trip_price = float(input("Enter the price of the trip: "))  # Total cost of the trip
puzzles = int(input("Enter the number of puzzles sold: "))  # Number of puzzles sold
dolls = int(input("Enter the number of talking dolls sold: "))  # Number of talking dolls sold
bears = int(input("Enter the number of teddy bears sold: "))  # Number of teddy bears sold
minions = int(input("Enter the number of minions sold: "))  # Number of minions sold
trucks = int(input("Enter the number of trucks sold: "))  # Number of trucks sold

# Step 1: Calculate the total number of toys sold
total_toys = puzzles + dolls + bears + minions + trucks  # Sum of all the toys sold

# Step 2: Calculate the total price for all the toys sold
total_price = (puzzles * puzzle_price) + (dolls * doll_price) + (bears * bear_price) + (minions * minion_price) + (trucks * truck_price)

# Step 3: Apply a 25% discount if the total number of toys is 50 or more
if total_toys >= 50:
    total_price *= 0.75  # Apply a 25% discount on the total price

# Step 4: Deduct 10% of the total revenue for the store rent
rent = total_price * 0.10  # 10% of the total revenue is taken as store rent
total_price_after_rent = total_price - rent  # Subtract rent from total price

# Step 5: Check if Sophie has enough money for the trip
if total_price_after_rent >= trip_price:
    # Sophie has enough money for the trip, calculate and print the remaining amount
    remaining_money = total_price_after_rent - trip_price
    print(f"Yes! {remaining_money:.2f} USD left.")
else:
    # Sophie does not have enough money, calculate and print the additional amount needed
    needed_money = trip_price - total_price_after_rent
    print(f"Not enough money! {needed_money:.2f} USD needed.")
