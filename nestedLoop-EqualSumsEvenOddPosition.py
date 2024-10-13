# 02. Equal Sums Even Odd Position

# Input: First number in the range
firstNum = int(input())

# Input: Second number in the range
secondNum = int(input())

# Loop through each number in the range from firstNum to secondNum (inclusive)
for number in range(firstNum, secondNum + 1):

    # Convert the current number to a string to access individual digits
    numberToString = str(number)

    # Initialize variables to store the sum of digits at even and odd positions
    evenSum = 0
    oddSum = 0

    # Enumerate through the digits of the current number
    for index, digit in enumerate(numberToString):

        # Convert the current digit back to an integer
        digit = int(digit)

        # If the index is even, add the digit to evenSum
        if index % 2 == 0:
            evenSum += digit

        # Otherwise, add the digit to oddSum
        else:
            oddSum += digit

    # After processing all digits, check if evenSum equals oddSum
    if evenSum == oddSum:
        # If the sums are equal, print the number followed by a space (without a new line)
        print(number, end=" ")
