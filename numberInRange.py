# 06. Number in Range
# Get the number as input from the user
number = int(input("Enter a number: "))

# Check if the number is in the range [-100, 100] and is not 0
# The number should be greater than or equal to -100 and less than or equal to 100, but not zero
if -100 <= number <= 100 and number != 0:
    print("Yes")
else:
    print("No")
