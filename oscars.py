# 6.	Oscars
# Input the actor's name
actorName = input()

# Input the initial academy points the actor has
academyPoints = float(input())

# Input the number of assessors who will evaluate the actor
assessorsNumber = int(input())

# Check if the actor already has more than 1250.5 points, which would qualify them for a nominee
if academyPoints > 1250.5:
    # If the actor has enough points, print a congratulatory message
    print(f"Congratulations, {actorName} got a nominee for leading role with {academyPoints:.1f}!")
else:
    # Loop through each assessor to add points based on their evaluation
    for i in range(assessorsNumber):
        # Input the assessor's name
        assessorsName = input()

        # Input the score that the assessor gives
        score = float(input())

        # Calculate the new points based on the length of the assessor's name and their score
        academyPoints += (len(assessorsName) * score) / 2

        # Check if the total points now exceed the required threshold of 1250.5
        if academyPoints > 1250.5:
            # If the points exceed the threshold, print a congratulatory message and stop further evaluations
            print(f"Congratulations, {actorName} got a nominee for leading role with {academyPoints:.1f}!")
            break

    # If the points are still below the threshold after all evaluations, print a message showing how many more points are needed
    if academyPoints <= 1250.5:
        print(f"Sorry, {actorName} you need {(1250.5 - academyPoints):.1f} more!")
