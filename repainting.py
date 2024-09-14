# 6. Repainting

# Reads the quantity of nylon, paint, and detergent required, as well as the number of working hours, converting all to integers.
nylonAmount = int(input())
paintAmount = int(input())
detergentQuantity = int(input())
workingHours = int(input())

# Adds 10% more paint to account for extra usage.
requiredPaint = (110 / 100) * paintAmount  # 10% of paint is added

# Adds 2 extra square meters of nylon as a safety margin.
requiredNylon = nylonAmount + 2  # 2m of nylon is added

# Calculates the total price of materials:
# - Nylon costs 1.50 per square meter.
# - Paint costs 14.50 per liter.
# - Detergent costs 5.00 per liter.
# - An additional fixed cost of 0.40 for miscellaneous supplies.
price = requiredNylon * 1.50 + requiredPaint * 14.50 + detergentQuantity * 5.00 + 0.40

# Calculates the labor cost per hour, which is 30% of the total material cost.
pricePerHour = (30 / 100) * price

# Calculates the total labor cost by multiplying the hourly rate by the number of working hours.
# Adds the total labor cost to the material cost to get the final price.
price = price + pricePerHour * workingHours

# Prints the final price for the repainting job.
print(price)
