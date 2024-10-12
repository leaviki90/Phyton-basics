# Bonus task
# This script prints a table of products where each cell is the product of its row and column index.
# The user inputs the number of rows (n) and columns (m), and the table is printed accordingly.

n = int(input("Enter the number of rows: "))  # Input: number of rows
m = int(input("Enter the number of columns: "))  # Input: number of columns

# Loop through the rows
for i in range(1, n + 1):  # Loop for rows from 1 to n
    # Loop through the columns
    for j in range(1, m + 1):  # Loop for columns from 1 to m
        print(
            i * j, end=" "
        )  # Print the product of the row and column, with a space after each value
    print()  # Move to the next line after each row is printed
