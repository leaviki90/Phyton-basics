#10.	Odd Even Sum
n = int(input())  # Input the number n, which indicates how many numbers the user will enter

evenSum = 0  # Initialize the sum for numbers at even indices
oddSum = 0   # Initialize the sum for numbers at odd indices

for i in range(0, n):  # Loop through n numbers, where i is the index
    num = int(input())  # Input the current number
    if i % 2 == 0:  # Check if the index is even
        evenSum += num  # If so, add the number to the even sum
    else:  # If the index is odd
        oddSum += num  # Add the number to the odd sum

# Check if the even and odd sums are equal
if evenSum == oddSum:
    print("Yes")  # If they are equal, print "Yes"
    print(f"Sum = {evenSum}")  # Print the sum (since both are equal)
else:
    print("No")  # If they are not equal, print "No"
    print(f"Diff = {abs(evenSum - oddSum)}")  # Print the absolute difference


