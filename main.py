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