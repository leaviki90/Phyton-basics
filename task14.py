# 5. Supplies for School

# Reads the number of pen packages and converts it to an integer.
pensPackage = int(input())

# Reads the number of marker packages and converts it to an integer.
markersPackage = int(input())

# Reads the number of liters of detergent and converts it to an integer.
litersDetergent = int(input())

# Reads the discount percentage and converts it to an integer.
reduction = int(input())

# Calculates the total price of all supplies without any discount.
# Pen package costs 5.80, marker package costs 7.20, and detergent costs 1.20 per liter.
price = pensPackage * 5.80 + markersPackage * 7.20 + litersDetergent * 1.20

# Calculates the discount and final amount to be paid after applying the discount.
pay = 100 - reduction  # Calculates the percentage to be paid after discount

# Calculates the final price by applying the discount.
finalPrice = (pay / 100) * price

# Prints the final price to be paid after the discount.
print(finalPrice)
