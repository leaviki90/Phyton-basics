# 3.	Combinations
# This script calculates the number of combinations of x1, x2, and x3
# such that their sum equals n, where each variable ranges from 0 to n.
# The user inputs the value of n, and the script counts all valid combinations.

n = int(input())  # Input: the value of n
count = 0  # Counter for the valid combinations

# Loop through all possible values of x1, x2, and x3 (from 0 to n)
for x1 in range(0, n + 1):  # Loop for x1
    for x2 in range(0, n + 1):  # Loop for x2
        for x3 in range(0, n + 1):  # Loop for x3
            if x1 + x2 + x3 == n:  # Check if the sum of x1, x2, and x3 equals n
                count += 1  # Increment the count if the condition is met

print(count)  # Output the total number of valid combinations
