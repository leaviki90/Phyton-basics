#1.	Day of Week
# Get the day of the week as an integer input from the user
dayOfWeek = int(input("Enter a number (1-7) to represent the day of the week: "))

# Dictionary mapping integers to corresponding days of the week
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# Print the day of the week based on user input, or "Error" if input is out of range
print(days.get(dayOfWeek, "Error"))
