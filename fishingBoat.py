# Fishing Trip Price Calculator

# Input the group's budget, the season, and the number of fishermen
groupBudget = int(input("Enter the group's budget: "))
season = input("Enter the season (spring, summer, autumn, winter): ").lower()  # Convert season input to lowercase
fishermanNum = int(input("Enter the number of fishermen: "))

# Initialize the total price variable
totalPrice = 0

# Determine the base price depending on the season
if season == "spring":
    totalPrice = 3000  # Base price for spring
elif season == "summer" or season == "autumn":
    totalPrice = 4200  # Base price for summer or autumn
elif season == "winter":
    totalPrice = 2600  # Base price for winter
else:
    # Handle invalid season input
    print("Error: Invalid season")
    exit()

# Apply discount based on the number of fishermen
if fishermanNum <= 6:
    totalPrice *= 0.9  # 10% discount if 6 or fewer fishermen
elif 7 <= fishermanNum <= 11:
    totalPrice *= 0.85  # 15% discount if between 7 and 11 fishermen
elif fishermanNum >= 12:
    totalPrice *= 0.75  # 25% discount if 12 or more fishermen
else:
    # Handle any unexpected error with the number of fishermen
    print("Error: Invalid number of fishermen")
    exit()

# Apply an additional 5% discount if it's not autumn and the number of fishermen is even
if season != "autumn" and fishermanNum % 2 == 0:
    totalPrice *= 0.95  # Additional 5% discount

# Check if the group's budget is enough and print the result
if groupBudget >= totalPrice:
    # If budget is sufficient, calculate how much is left
    print(f"Yes! You have {groupBudget - totalPrice:.2f} USD left.")
else:
    # If budget is not sufficient, calculate how much more is needed
    print(f"Not enough money! You need {totalPrice - groupBudget:.2f} USD.")
