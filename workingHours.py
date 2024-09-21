# 7.	Working Hours
# Get the hours and day as input from the user
hours = int(input("Enter the hours: "))
day = input("Enter the day: ")

# Check if the hours are between 10 and 18, and the day is not Sunday
if 10 <= hours <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")
