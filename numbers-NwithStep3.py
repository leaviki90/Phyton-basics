#2.	Numbers 1...N with Step 3
# Take an integer input from the user and store it in the variable 'number'
number = int(input())

# Loop starting from 1 up to 'number' (inclusive), with a step of 3
# '1' is the starting point, 'number + 1' is the end (non-inclusive), and '3' is the step size
for i in range(1, number + 1, 3):
    # Print the current value of 'i'
    print(i)

# Note:
# range(1, 101) is the same as range(1, 101, 1), but when the step is 1, it can be omitted
