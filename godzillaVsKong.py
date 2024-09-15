#5.	Godzilla vs. Kong
# Input Section
budget = float(input("Enter the movie budget (1.00 - 1000000.00 USD): "))  # Total movie budget
extras = int(input("Enter the number of extras (1 - 500): "))  # Number of extras
clothingPerOne = float(input("Enter the price for clothing per extra (1.00 - 1000.00 USD): "))  # Price for clothing per extra

# Step 1: Calculate the cost of the movie set, which is 10% of the total budget
movieSet = budget * 0.10  # 10% of the budget is allocated for the set

# Step 2: Calculate the total clothing cost for all extras
clothingCost = extras * clothingPerOne  # Total cost for clothing

# Step 3: Apply a 10% discount on clothing if there are more than 150 extras
if extras > 150:
    clothingCost *= 0.90  # 10% discount on clothing for more than 150 extras

# Step 4: Calculate the total expense (set + clothing)
totalExpense = movieSet + clothingCost  # Total cost for set and clothing

# Step 5: Compare the total expense with the budget and print the appropriate result
if totalExpense <= budget:
    # If total expense is within or equal to the budget
    moneyLeft = budget - totalExpense  # Calculate the money left
    print("Action!")
    print(f"Wingard starts filming with {moneyLeft:.2f} USD left.")  # Output formatted to 2 decimal places
else:
    # If total expense exceeds the budget
    moneyNeeded = totalExpense - budget  # Calculate how much more is needed
    print("Not enough money!")
    print(f"Wingard needs {moneyNeeded:.2f} USD more.")  # Output formatted to 2 decimal places
