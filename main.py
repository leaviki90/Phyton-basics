# Division with a decimal result
a = 24 / 9
print(a)  # This will print the exact result of division

# Floor division (integer division)
b = 24 // 9  # This will return the largest integer that is less than or equal to the division result
print(b)

# Modulus operator (remainder of division)
c = 24 % 9  # This will return the remainder of the division
print(c)

# Note: Division by zero is not allowed in Python and will raise a ZeroDivisionError if attempted

# Concatenating a string and a number can cause an error
# You need to convert the number to a string using str()

b = 3  # b is a variable with a numeric value

# The following would cause a TypeError without using str():
# print("Ana" + b)  # This would raise an error

# Correct way:
print("Ana" + str(b))  # This converts the number to a string before concatenating

# In Python, a variable can change its type dynamically

x = 5  # x is initially an integer
print(x)  # prints the value of x, which is 5
x = "Hello World"  # x is now a string
print(x)  # prints the value of x, which is "Hello World"

# It is not allowed to have spaces between words in a variable name
# A variable name cannot start with a number
# A variable name cannot contain special characters (e.g., !, @, #, $, etc.)
# Variable names can include uppercase letters, lowercase letters, and numbers
# CamelCase or snake_case is often used for naming variables (e.g., myVariable or my_variable)

#print(f"{(10/3):.3f}");
# The f-string here would format the result of 10/3 to 3 decimal places, displaying it as 3.333.

# Input is by default a string, meaning whatever the user enters is read as a string.
# This is why we don't need to explicitly convert it to a string using str().

# For rounding numbers:

# Ceil (ceiling) 4.21 => 5, 4.86 => 5 from the Math module
# It rounds the number up to the nearest integer.

# Floor 4.21 => 4, 4.86 => 4 from the Math module
# It rounds the number down to the nearest integer.

# Round to the nearest integer:
# Round 4.21 => 4, 4.86 => 5
# The `round()` function rounds to the closest integer.

# Abs (absolute value):
# abs(+3) => 3, abs(-3) => 3

# Example of TypeError:
# print(1 + 2 + 3 + "4" + 1)
# Python does not allow implicit type conversion (coercion).
# It won't automatically convert one data type to another (like adding an integer to a string).
# This would raise a TypeError.

# To avoid the error, explicitly convert types:
print(str(1 + 2 + 3) + "4" + str(1))
# OR explicitly state what we want:
print(1 + 2 + 3 + int(4) + 1)

# Logical expressions

nowItRains = False
weHaveClassPython = True

# The following expression evaluates if 3 + 4 is greater than 5 (which is True)
expression = 3 + 4 > 5  # True

# The following expression evaluates if 4*2 - 3 is equal to 8 + 1 (which is False)
expression2 = 4 * 2 - 3 == 8 + 1  # False

# Print the results of the logical expressions
print(expression)  # True
print(expression2)  # False

# Arithmetic operators have a higher precedence than relational (comparison) operators.
# For example, in an expression like 3 + 4 > 5, the addition happens first, then the comparison.

# Less than or equal to is written as <=
# Greater than or equal to is written as >=
