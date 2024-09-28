#8.	Number sequence
# Read an integer 'n', which tells us how many numbers we will input
n = int(input())

# Read the first number, which will initially be both the minimum and maximum
minNum = int(input())  # This is the first number, assumed to be both min and max initially
maxNum = minNum  # Since it's the only number so far, it is also the maximum

# Now we process the remaining n - 1 numbers
# For each number, we check if it's smaller than the current min or larger than the current max
for i in range(1, n):  # Start from 1 because the first number is already read and doesn't enter the loop
    num = int(input())  # Read the next number
    if num < minNum:
        minNum = num  # Update minNum if the current number is smaller
    if num > maxNum:
        maxNum = num  # Update maxNum if the current number is larger

# After the loop, print the largest and smallest numbers
print(f"Max number: {maxNum}")
print(f"Min number: {minNum}")

