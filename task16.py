# 7. Food Delivery

# Reads the number of chicken, fish, and vegetarian menus ordered, converting each to an integer.
chickenMenu = int(input())
fishMenu = int(input())
vegetarianMenu = int(input())

# Calculates the total price of the ordered menus:
# - Chicken menu costs 10.35 per menu.
# - Fish menu costs 12.40 per menu.
# - Vegetarian menu costs 8.15 per menu.
price = chickenMenu * 10.35 + fishMenu * 12.40 + vegetarianMenu * 8.15

# Calculates the price of the dessert, which is 20% of the total price of the menus.
dessert = (20 / 100) * price  # Dessert is 20% of the price

# Adds the dessert price and the fixed delivery fee of 2.50 to the total price.
price = price + dessert + 2.50

# Prints the final price, which includes the cost of menus, dessert, and delivery.
print(price)
