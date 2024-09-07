#5.	Greetings by Name
# User inputs their name
name = input()

# First way: Concatenation of strings
a = "Hello, " + name + "!"  # The name is concatenated with the greeting
#print(a)  # Uncomment this to print the result

# You can also print directly without assigning to a variable
# print("Hello, " + ime + "!")

# Second way: Using f-string formatting, which allows embedding expressions inside {}
print(f"Hello, {name}!")  # The name is included directly in the string using an f-string
