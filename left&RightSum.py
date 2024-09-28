#9.	Left and Right Sum
# Read an integer 'n' from user input, which represents the number of values to sum for each side
n = int(input())

# We initialize the first sum (sum1) and a variable to store input numbers (num1)
sum1 = 0
num1 = 0

# Read the first 'n' numbers from input and sum them up in sum1
for i in range(0, n):
    num1 = int(input())  # Read each number
    sum1 += num1  # Add the number to sum1

# We initialize the second sum (sum2) and a variable to store input numbers (num2)
sum2 = 0
num2 = 0

# Read the next 'n' numbers from input and sum them up in sum2
for i in range(0, n):
    num2 = int(input())  # Read each number
    sum2 += num2  # Add the number to sum2

# Compare the two sums (sum1 and sum2)
if sum1 == sum2:
    # If the sums are equal, print 'Yes' and the sum value
    print(f"Yes, sum = {sum1}")
else:
    # If the sums are not equal, print 'No' and the absolute difference between the sums
    print(f"No, diff = {abs(sum1 - sum2)}")






