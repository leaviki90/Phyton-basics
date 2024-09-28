#3.	Even Powers of 2
# Example loop with negative step (decrements by 2 from 15 to 1)
# for i in range(15, 0, -2):
#    print(i, end=" ")  # Prints all numbers in a single line, separated by space

# ** means exponentiation (raising a number to a power)

# Take user input for the highest exponent
highestExponent = int(input())

# Loop from 0 to the input number (inclusive) with step 2
# This ensures only even exponents (0, 2, 4, ...) are used
for i in range(0, highestExponent + 1, 2):
    # Print 2 raised to the power of the current 'i'
    print(2**i)

