# Operations Between Numbers

# Get the two numbers and the operator from user input
N1 = int(input("Enter the first number: "))
N2 = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %): ")

# Initialize the result variable
result = 0

# Perform the operation based on the operator input
if operator == "+":
    # Addition operation
    result = N1 + N2
    # Check if the result is even or odd
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

elif operator == "-":
    # Subtraction operation
    result = N1 - N2
    # Check if the result is even or odd
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

elif operator == "*":
    # Multiplication operation
    result = N1 * N2
    # Check if the result is even or odd
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

elif operator == "/":
    # Division operation
    if N2 == 0:
        # Handle division by zero case
        print(f"Cannot divide {N1} by zero")
    else:
        # Perform the division and display the result formatted to 2 decimal places
        result = N1 / N2
        print(f"{N1} {operator} {N2} = {result:.2f}")

elif operator == "%":
    # Modulus operation
    if N2 == 0:
        # Handle division by zero case for modulus
        print(f"Cannot divide {N1} by zero")
    else:
        # Perform the modulus operation and display the result
        result = N1 % N2
        print(f"{N1} {operator} {N2} = {result}")

else:
    # Handle invalid operator input
    print("Invalid operator!")
