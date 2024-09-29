#2.	Half Sum Element
# Input the number of total values to be entered
n = int(input())

# Input the first number and initialize it as the largest number
largestNum = int(input())

# Initialize the sum to include the first number
sum1 = largestNum

# Initialize a variable to hold the current number
num = 0

# Loop through the remaining (n-1) numbers
for i in range(1, n):
    # Input the current number
    num = int(input())

    # Add the current number to the total sum
    sum1 += num

    # Update the largest number if the current number is greater than the largest so far
    if num > largestNum:
        largestNum = num

# Check if the largest number equals the sum of all other numbers (total sum minus the largest number)
if largestNum == (sum1 - largestNum):
    # If true, print "Yes" and the sum that equals the largest number
    print("Yes")
    print(f"Sum = {largestNum}")
else:
    # If false, print "No" and the absolute difference between the largest number and the sum of the other numbers
    print("No")
    print(f"Diff = {abs(sum1 - largestNum - largestNum)}")
