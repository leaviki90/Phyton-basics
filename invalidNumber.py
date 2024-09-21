#10.	Invalid Number

# Read an integer entered by the user
number = int(input("Enter a number: "))

# Check if the number is valid
if not (100 <= number <= 200 or number == 0):
    print("invalid")

# Old code for reference
# number = int(input())
# if number < 100 or number > 200 and number != 0:
#     print("invalid")

