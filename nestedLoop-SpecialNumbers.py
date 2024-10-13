# 5. Special Numbers

# Input: An integer n
n = int(input())

# Loop through all four-digit numbers from 1111 to 9999
for num in range(1111, 10000):

    # Assume the number is special initially
    is_special = True

    # Check each digit of the current number
    for digit in str(num):

        # Convert the digit back to an integer
        digit = int(digit)

        # If any digit is 0 or n is not divisible by the digit, the number is not special
        if digit == 0 or n % digit != 0:
            is_special = False
            break

    # If the number is still considered special, print it
    if is_special:
        print(f"{num}", end=" ")
