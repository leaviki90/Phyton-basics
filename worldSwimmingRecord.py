#6.	World Swimming Record
import math  # Import math module for floor function

# Input Section
record = float(input("Enter the current world record time (in seconds): "))  # Current world record time in seconds
distanceM = float(input("Enter the distance to be covered (in meters): "))  # Distance to be covered in meters
secondsM = float(input("Enter the time per meter (in seconds): "))  # Time it takes to cover one meter

# Step 1: Calculate the total time required to cover the distance without delays
time = distanceM * secondsM  # Total time for the distance at constant speed

# Step 2: Calculate the slowing down effect
# The runner slows down every 15 meters, adding 12.5 seconds each time
slowingDown = math.floor(distanceM / 15) * 12.5  # Number of slowdowns * 12.5 seconds

# Step 3: Calculate the total time, including slowdowns
total = time + slowingDown  # Final total time

# Step 4: Compare the total time with the world record
if total < record:
    # If the total time is less than the record, print a success message with the new record
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    # If the total time is greater than or equal to the record, print a failure message with the excess time
    print(f"No, he failed! He was {(total - record):.2f} seconds slower.")

