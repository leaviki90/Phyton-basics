# 9. Yard Greening

# Reads the input from the user, which is the area in square meters to be landscaped. Converts it to a float to allow for decimal values.
landscapeSquareMeters = float(input())

# Calculates the initial service price based on the area (7.61 USD per square meter).
servicePrice = landscapeSquareMeters * 7.61

# Calculates the discount (18% of the service price).
discountPrice = servicePrice * 0.18

# Subtracts the discount from the service price to get the final price.
finalServicePrice = servicePrice - discountPrice

# Prints the final price, formatted as a string with the currency "USD".
print(f"The final price is: {finalServicePrice} USD.")
