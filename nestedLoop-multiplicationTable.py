# 2.	Multiplication Table
# This script prints a multiplication table from 1 to 10.
# The outer loop (i) iterates through numbers 1 to 10 for the rows.
# The inner loop (j) iterates through numbers 1 to 10 for the columns.

for i in range(1, 11):  # Loop for rows (numbers 1 to 10)
    for j in range(1, 11):  # Loop for columns (numbers 1 to 10)
        print(f"{i} * {j} = {i * j}")  # Print the result of multiplying i and j
