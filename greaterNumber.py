#2.	Greater Number
# Prompt the user to input two integers
firstEntry = int(input())
secondEntry = int(input())

# Compare the two integers and print the larger one with a label
if firstEntry >= secondEntry:
    # If the first number is greater than or equal to the second number, print the first number with "bu"
    print(firstEntry, "First")
else:
    # If the second number is greater, print the second number with "second"
    print(secondEntry, "Second")
