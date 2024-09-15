#1.	Sum Seconds
# Input: Read three time intervals in seconds
first = int(input("Enter the first time (in seconds): "))
second = int(input("Enter the second time (in seconds): "))
third = int(input("Enter the third time (in seconds): "))

# Step 1: Calculate the total time in seconds
total = first + second + third  # Sum of all three times

# Step 2: Convert the total time to minutes and seconds
minutes = total // 60  # Get the number of full minutes
seconds = total % 60  # Get the remaining seconds

# Step 3: Print the result in the format "minutes:seconds"
# If seconds is less than 10, add a leading zero for formatting
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


