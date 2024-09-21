#8.	Cinema Ticket
# Get user input for the day of the week
day = input("Enter one day in a week: ")

# Dictionary mapping days of the week to movie ticket prices
weekDays = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16
}

# Fetch the price from the dictionary; if the day is not found, return a default message
price = weekDays.get(day, "No such a day")

# Output the price or the error message
print(price)



