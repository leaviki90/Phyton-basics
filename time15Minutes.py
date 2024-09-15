#3.	Time + 15 Minutes
# Input: Read the current time in hours and minutes
hours = int(input("Enter hours (0-23): "))  # Hours between 0 and 23
minutes = int(input("Enter minutes (0-59): "))  # Minutes between 0 and 59

# Step 1: Add 15 minutes to the current time
minutes = minutes + 15

# Step 2: Adjust the time if minutes are 60 or more
if minutes >= 60:
    minutes -= 60  # Subtract 60 minutes to reset minute count
    hours += 1  # Increase the hour by 1

    # Step 3: Handle hour overflow when it reaches 24
    if hours == 24:
        hours = 0  # Reset hour to 0 if it reaches 24

# Step 4: Format and print the result
# If minutes are less than 10, we add a leading zero to keep the format consistent
if minutes >= 10:
    print(f"{hours}:{minutes}")
else:
    print(f"{hours}:0{minutes}")

