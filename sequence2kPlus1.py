#4.	Sequence 2k + 1
# Prompt the user to enter a number 'n'
n = int(input())

# Initialize 'currentNum' to 1, which will be the starting point
currentNum = 1

# Keep looping as long as 'currentNum' is less than or equal to 'n'
while currentNum <= n:
    # Print the current value of 'currentNum'
    print(currentNum)

    # Update 'currentNum' by multiplying it by 2 and adding 1 in each iteration
    currentNum = 2 * currentNum + 1
