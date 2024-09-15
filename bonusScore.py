#2.	Bonus Score
# Input: Read the starting number
startingNum = int(input("Enter a starting number: "))

# Initialize the bonus score
bonusScore = 0

# Step 1: Base bonus points calculation
if startingNum <= 100:
    # If the number is less than or equal to 100, a fixed bonus of 5 points is given
    bonusScore = 5
elif startingNum > 1000:
    # If the number is greater than 1000, 10% of the number is given as a bonus
    bonusScore = 0.10 * startingNum
else:
    # For numbers between 101 and 1000, 20% of the number is given as a bonus
    bonusScore = 0.20 * startingNum

# Step 2: Additional bonus points
# If the number is even, add 1 bonus point
if startingNum % 2 == 0:
    bonusScore += 1

# If the number ends in 5, add 2 bonus points
if startingNum % 10 == 5:
    bonusScore += 2

# Output the results
print(f"Bonus score: {bonusScore:.1f}")  # Print the total bonus score (formatted to 1 decimal)
print(f"Total score: {bonusScore + startingNum:.1f}")  # Print the final score (starting number + bonus)


