# Coins

# Initialize the amount to be divided into coins
amount = float(input("Enter the amount in EUR: "))
count = 0  # Count how many coins are used

# List of available coins, ordered from largest to smallest
coins = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

# While there is still some amount to break down into coins
for coin in coins:
    # Use as many of the current coin as possible
    while amount >= coin:
        amount = round(
            amount - coin, 2
        )  # Subtract coin value from the amount (rounded to avoid floating point issues)
        count += 1  # Increment coin count

# Output the total number of coins used
print(f"Total number of coins used: {count}")
