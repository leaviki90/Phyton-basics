# 03. New House

# Input the type of flowers, number of flowers, and the budget
typeOfFlowers = input()
numberOfFlowers = int(input())
budget = int(input())

# Prices per flower for each flower type
pricePerFlower = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50
}

# Check if the flower type is valid
if typeOfFlowers in pricePerFlower:

    # Calculate the total price without discounts or surcharges
    totalPrice = numberOfFlowers * pricePerFlower[typeOfFlowers]

    # Apply discounts or surcharges based on the number of flowers and the type
    if typeOfFlowers == "Roses" and numberOfFlowers > 80:
        totalPrice *= 0.90  # 10% discount for Roses if more than 80
    elif typeOfFlowers == "Dahlias" and numberOfFlowers > 90:
        totalPrice *= 0.85  # 15% discount for Dahlias if more than 90
    elif typeOfFlowers == "Tulips" and numberOfFlowers > 80:
        totalPrice *= 0.85  # 15% discount for Tulips if more than 80
    elif typeOfFlowers == "Narcissus" and numberOfFlowers < 120:
        totalPrice *= 1.15  # 15% surcharge for Narcissus if fewer than 120
    elif typeOfFlowers == "Gladiolus" and numberOfFlowers < 80:
        totalPrice *= 1.20  # 20% surcharge for Gladiolus if fewer than 80

    # Check if the budget is enough for the total price
    if budget >= totalPrice:
        remainingMoney = budget - totalPrice  # Calculate the remaining money
        # Print the success message with remaining money
        print(f"Hey, you have a great garden with {numberOfFlowers} {typeOfFlowers} and {remainingMoney:.2f} USD left.")
    else:
        neededMoney = totalPrice - budget  # Calculate the money needed
        # Print the failure message with the amount of money needed
        print(f"Not enough money, you need {neededMoney:.2f} USD more.")
else:
    # If the flower type is invalid, print an error message
    print("Invalid flower type!")
