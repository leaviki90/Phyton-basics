#5.	Numbers from 100 to 200
# Prompt the user to input an integer number
checkTheNumber = int(input())

# Check and print the category based on the input number
if checkTheNumber < 100:
    # If the number is less than 100
    print("Less than 100")
elif checkTheNumber > 200:
    # If the number is greater than 200
    print("Greater than 200")
else:
    # If the number is between 100 and 200 (inclusive)
    print("Between 100 and 200")
