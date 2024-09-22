# 9. Ski Trip Price Calculator

# Get the number of days for the ski trip from user input
daysOfStay = int(input("Enter the number of days: "))

# Get the type of room from user input
roomType = input("Enter room type (room for one person/apartment/president apartment): ")

# Get the feedback (positive or negative) from user input
grade = input("Enter feedback (positive/negative): ")

# Dictionary containing the base price per night for each room type
rooms = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}

# Calculate the number of nights (one less than the number of days)
nights = daysOfStay - 1

# Calculate the total price based on the room type and number of nights
totalPrice = nights * rooms[roomType]

# Apply discounts based on the type of room and length of stay
if roomType == "apartment":
    if daysOfStay < 10:
        totalPrice *= 0.70  # 30% discount
    elif 10 <= daysOfStay <= 15:
        totalPrice *= 0.65  # 35% discount
    else:
        totalPrice *= 0.50  # 50% discount
elif roomType == "president apartment":
    if daysOfStay < 10:
        totalPrice *= 0.90  # 10% discount
    elif 10 <= daysOfStay <= 15:
        totalPrice *= 0.85  # 15% discount
    else:
        totalPrice *= 0.80  # 20% discount

# Adjust the total price based on the feedback received
if grade == "positive":
    totalPrice *= 1.25  # Increase total by 25% for positive feedback
elif grade == "negative":
    totalPrice *= 0.90  # Decrease total by 10% for negative feedback

# Print the final price rounded to 2 decimal places
print(f"{totalPrice:.2f}")
