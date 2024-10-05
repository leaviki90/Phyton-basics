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

# A method is associated with a type or class
# - A method is a function that is called on an object, and it's associated with the object's class.
# - For example, methods like lower() are defined for string objects in Python.
# - Methods belong to specific data types (like strings, lists, dictionaries, etc.).

# A function is independent of objects and can be called on its own
# - Functions are general-purpose and can be applied to various types of data or used in different contexts.

# Example of a method: lower()
# - lower() is a string method that converts all uppercase letters in the string to lowercase.
# - This method does not modify the original string, it returns a new string in lowercase.

# Example:
text = "Hello World"
lowercase_text = text.lower()  # Returns a new string "hello world"

# In Python, strings are immutable
# - This means that once a string is created, it cannot be changed.
# - Any operation that modifies a string, such as lower(), actually creates a new string.
# - The original string remains unchanged.

# Example:
original_string = "Python"
new_string = original_string.lower()  # new_string is "python", original_string is still "Python"

# Immutable objects like strings ensure that their values don't change, making code safer and easier to debug.

# Explanation of the priority of logical operators
# 1. "not" has the highest priority (unary operator)
# 2. "and" has the next highest priority (requires two expressions)
# 3. "or" has the lowest priority (also requires two expressions)

# Let's see how this works in practice:
expression3 = not 3 > 4 and 4 == 5 or not 2 != 3 or not 1 == 2
# 1. not 3 > 4 becomes True (because 3 > 4 is False, and not False is True)
# 2. not 2 != 3 becomes False (because 2 != 3 is True, and not True is False)
# 3. not 1 == 2 becomes True (because 1 == 2 is False, and not False is True)
# Now the expression becomes: True and False or False or True
# Next, the "and" operator is evaluated first: True and False -> False
# Now we have: False or False or True
# Finally, "or" is evaluated: False or False -> False, then False or True -> True
print(expression3)  # Output: True

# Another simple expression example:
expression4 = not 2 + 3 == 4
# This is equivalent to: not (2 + 3 == 4), because "==" has higher priority than "not"
# 2 + 3 == 4 is False, so not False becomes True
print(expression4)  # Output: True

#price = 5.6789
#print(f"{price:.2f}")  # Prints: 5.68
#print(f"{(rowNumber * colNumber * 5):.2f} USD")

# The 'for' loop starts from 2, increments by 7, and stops before reaching 10
for i in range(2, 10, 7):
    print(i)

# The 'for' loop does not accept decimal step values, but a 'while' loop can handle them

# Initialize the variable 'i' with the starting value of 2
i = 2
# The 'while' loop continues as long as 'i' is less than 10
while i < 10:
    # Print the current value of 'i'
    print(i)
    # Increment 'i' by 7 after each iteration (the step)
    i += 7
