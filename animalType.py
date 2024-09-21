#3.	Animal Type
# This program prints the species of the animal based on the user's input.
# 1. If the input is "dog", it prints "mammal".
# 2. If the input is "crocodile", "tortoise", or "snake", it prints "reptile".
# 3. For any other input, it prints "unknown".

# Get the animal name from user input
animal = input("Enter the name of an animal: ")

# Check the input and determine the species
if animal == "dog":
    print("mammal")

# Check if the animal is one of the reptiles: "crocodile", "tortoise", or "snake"
# Using 'in' with a list improves readability and avoids multiple 'or' conditions.
# Old way using 'or':
# elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
#     print("reptile")
elif animal in ["crocodile", "tortoise", "snake"]:
    print("reptile")
else:
    print("unknown")

