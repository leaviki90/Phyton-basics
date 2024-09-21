#02. Weekend or Working Day
# Dictionary mapping days of the week to either "Working day" or "Weekend"
days = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend"
}

# Get the day as input from the user
day = input("Enter a day of the week: ")

# Print whether the day is a "Working day" or "Weekend", or "Error" if the input is invalid
print(days.get(day, "Error"))

