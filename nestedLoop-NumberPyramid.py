# 1.	Number Pyramid

# Prompt the user to enter a number and convert the input to an integer
n = int(input("Enter a number: "))

# Initialize the starting number for the pyramid
current = 1

# Initialize a flag to determine when to stop printing numbers
is_current_bigger_than_n = False

# Loop through the number of rows from 1 to n (inclusive)
for row in range(1, n + 1):

    # Loop through the columns for the current row (1 to row, inclusive)
    for col in range(1, row + 1):

        # Check if the current number exceeds n
        if current > n:
            # Set the flag to True if the current number exceeds n
            is_current_bigger_than_n = True
            # Break out of the inner loop
            break

        # Print the current number followed by a space, without moving to the next line
        print(current, end=" ")

        # Increment the current number for the next iteration
        current += 1

    # Check if the flag is set to True, indicating that printing should stop
    if is_current_bigger_than_n:
        # Break out of the outer loop
        break

    # Print a newline to move to the next row of the pyramid
    print()
