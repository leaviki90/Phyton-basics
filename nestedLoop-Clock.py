# Clock

# Outer loop to iterate through each hour of the day (0-23)
for h in range(24):

    # Inner loop to iterate through each minute of the current hour (0-59)
    for m in range(60):
        # Print the current hour and minute in the format "hour:minute"
        print(f"{h}:{m}")
