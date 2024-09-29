#8. Tennis Ranklist
# Input the number of tournaments the player has participated in
tournamentsNum = int(input())

# Input the initial points the player starts with
initialPoints = int(input())

# Initialize variables
# 'stage' will hold the stage reached in each tournament (either "W", "F", or "SF")
stage = ""
# 'points' will accumulate the total points earned from tournaments
points = 0
# 'stageCount' will count the total number of tournaments played
stageCount = 0
# 'winnerCount' will count the number of tournaments won ("W" stages)
winnerCount = 0

# Loop through each tournament
for i in range(1, tournamentsNum + 1):
    # Input the tournament stage reached
    stage = input()

    # If the player won the tournament ("W"), add 2000 points and increment win and stage counters
    if (stage == "W"):
        points += 2000
        stageCount += 1
        winnerCount += 1

    # If the player reached the final ("F"), add 1200 points and increment the stage counter
    if (stage == "F"):
        points += 1200
        stageCount += 1

    # If the player reached the semi-final ("SF"), add 720 points and increment the stage counter
    if (stage == "SF"):
        points += 720
        stageCount += 1

# Calculate the final total points by adding initial points to points earned from tournaments
totalPoints = initialPoints + points

# Calculate the average points per tournament by dividing total points earned by the number of tournaments played
averagePoints = points // stageCount

# Calculate the percentage of tournaments won (W) by dividing wins by the number of tournaments played and multiplying by 100
totalWin = (winnerCount / stageCount) * 100

# Print the final total points after all tournaments
print(f"Final points: {totalPoints}")

# Print the average points earned per tournament, rounded to the nearest integer
print(f"Average points: {round(averagePoints)}")

# Print the percentage of tournaments won, rounded to two decimal places
print(f"{totalWin:.2f}%")

