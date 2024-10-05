#3.	Sum Numbers
# Initialize the first input as the target sum
target_sum = int(input("Enter the target sum: "))

sum1 = 0  # Set the initial sum to 0

# Keep asking for numbers and adding to the sum
while True:
    num = int(input())  # Get a new number to add
    sum1 += num  # Add the number to the total sum

    # Check if the sum has reached or exceeded the target sum
    if sum1 >= target_sum:
        print(f"Total sum is: {sum1}")
        break  # Exit the loop once the condition is met


