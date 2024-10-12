# 4.	Sum of Two Numbers
# This script finds two numbers within a given interval that sum up to a magic number.
# It also counts all possible combinations of two numbers within the interval.

startInterval = int(input())  # Input: start of the interval
endInterval = int(input())  # Input: end of the interval
magicNumber = int(input())  # Input: magic number we are looking for
count = 0  # Counter for the number of combinations

found = False  # Flag to check if a combination has been found

# Loop through all combinations of two numbers in the interval
for i in range(startInterval, endInterval + 1):  # Loop for the first number
    for j in range(startInterval, endInterval + 1):  # Loop for the second number
        count += 1  # Increment combination count
        if i + j == magicNumber:  # Check if the sum equals the magic number
            print(f"Combination N:{count} ({i} + {j} = {magicNumber})")
            found = True  # Set flag to True if a combination is found
            break  # Stop once the first combination is found
    if found:  # Break outer loop if a combination has been found
        break

if not found:  # If no combination was found
    print(f"{count} combinations - neither equals {magicNumber}")
