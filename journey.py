# Journey Budget Planner

# Input the budget and season from the user
budget = float(input("Enter your budget: "))
season = input("Enter the season (summer/winter): ")

# Initialize variables for destination, money spent, and type of holiday
destination = ""
moneySpent = 0
typeOfHoliday = ""

# Determine the destination and type of holiday based on budget and season
if budget <= 100:
    # If the budget is up to 100, the destination is Serbia
    destination = "Serbia"
    if season == "summer":
        moneySpent = budget * 0.30  # Spend 30% of the budget in summer
        typeOfHoliday = "Camp"
    elif season == "winter":
        moneySpent = budget * 0.70  # Spend 70% of the budget in winter
        typeOfHoliday = "Hotel"
    else:
        # Handle invalid season input
        print("Invalid season")
        exit()

elif 100 < budget <= 1000:
    # If the budget is between 100 and 1000, the destination is Balkans
    destination = "Balkans"
    if season == "summer":
        moneySpent = budget * 0.40  # Spend 40% of the budget in summer
        typeOfHoliday = "Camp"
    elif season == "winter":
        moneySpent = budget * 0.80  # Spend 80% of the budget in winter
        typeOfHoliday = "Hotel"
    else:
        # Handle invalid season input
        print("Invalid season")
        exit()

elif budget > 1000:
    # If the budget is greater than 1000, the destination is Europe
    destination = "Europe"
    moneySpent = budget * 0.90  # Spend 90% of the budget
    typeOfHoliday = "Hotel"

else:
    # Handle any unexpected errors with budget input
    print("Error with budget input")
    exit()

# Output the destination and the amount spent, formatted to 2 decimal places
print(f"Somewhere in {destination}")
print(f"{typeOfHoliday} - {moneySpent:.2f}")
