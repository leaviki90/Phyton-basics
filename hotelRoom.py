# Hotel Room Price Calculator

# Get the month of stay and the number of nights from user input
month = input("Enter the month of stay (May, October, June, September, etc.): ")
nightsNum = int(input("Enter the number of nights: "))

# Initialize variables for studio and apartment prices
studio = 0.0
apartment = 0.0

# Determine the base prices and apply discounts based on the month and number of nights
if month == "May" or month == "October":
    # Base prices for May and October
    studio = 50 * nightsNum
    apartment = 65 * nightsNum
    # Apply discount for studio if staying more than 14 nights
    if nightsNum > 14:
        studio *= 0.70  # 30% discount
    # Apply discount for studio if staying more than 7 nights
    elif nightsNum > 7:
        studio *= 0.95  # 5% discount
elif month == "June" or month == "September":
    # Base prices for June and September
    studio = 75.20 * nightsNum
    apartment = 68.70 * nightsNum
    # Apply discount for studio if staying more than 14 nights
    if nightsNum > 14:
        studio *= 0.80  # 20% discount
else:
    # Base prices for other months (e.g., July, August, etc.)
    studio = 76 * nightsNum
    apartment = 77 * nightsNum

# Apply discount for apartment if staying more than 14 nights
if nightsNum > 14:
    apartment *= 0.90  # 10% discount

# Output the final prices for the apartment and studio, rounded to 2 decimal places
print(f"Apartment: {apartment:.2f} USD.")
print(f"Studio: {studio:.2f} USD.")
