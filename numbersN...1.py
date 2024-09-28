#04. Numbers N...1
# Read an integer 'number' from user input
number = int(input())

# Loop starting from 'number', counting down to 1 (inclusive) with a step of -1
for i in range(number, 0, -1):
    # Print each number on the same line, separated by a space
    print(i, end=" ")
