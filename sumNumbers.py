#7.	Sum Numbers

# Read an integer 'n' from user input, which represents how many numbers will be entered
n = int(input())  # koliko brojeva unosimo

# Initialize a variable 'sum' to store the total sum of the entered numbers
sum = 0

# Initialize 'number' to hold the current number input by the user
number = 0

# Loop from 1 to n (inclusive) to read 'n' numbers from the user
for i in range(1, n+1):  #or for i in range(0, n):
    number = int(input())
    sum += number

# After the loop, print the final sum of all entered numbers
print(sum)



