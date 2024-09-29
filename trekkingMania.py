#7. Trekking Mania
# Input the number of groups participating in the trekking
numberOfGroups = int(input())

# Initialize variables for each group category
# 'firstGroup' represents groups with 5 or fewer people
firstGroup = 0
# 'secondGroup' represents groups with 6 to 12 people
secondGroup = 0
# 'thirdGroup' represents groups with 13 to 25 people
thirdGroup = 0
# 'fourthGroup' represents groups with 26 to 40 people
fourthGroup = 0
# 'fifthGroup' represents groups with 41 or more people
fifthGroup = 0
# 'totalPeople' will hold the total number of participants across all groups
totalPeople = 0

# Loop through each group to classify based on the number of people in each group
for i in range(1, numberOfGroups + 1):
    # Input the number of people in the current group
    peopleInGroup = int(input())

    # Classify the group based on the number of people and increment the corresponding category
    if peopleInGroup <= 5:
        firstGroup += peopleInGroup
    elif 6 <= peopleInGroup <= 12:
        secondGroup += peopleInGroup
    elif 13 <= peopleInGroup <= 25:
        thirdGroup += peopleInGroup
    elif 26 <= peopleInGroup <= 40:
        fourthGroup += peopleInGroup
    elif peopleInGroup >= 41:
        fifthGroup += peopleInGroup

# Calculate the total number of participants from all groups
totalPeople = firstGroup + secondGroup + thirdGroup + fourthGroup + fifthGroup

# Print the percentage of people in each group category, rounded to two decimal places
print(f"{(firstGroup / totalPeople) * 100:.2f}%")  # Percentage of people in groups of 5 or fewer
print(f"{(secondGroup / totalPeople) * 100:.2f}%")  # Percentage of people in groups of 6 to 12
print(f"{(thirdGroup / totalPeople) * 100:.2f}%")  # Percentage of people in groups of 13 to 25
print(f"{(fourthGroup / totalPeople) * 100:.2f}%")  # Percentage of people in groups of 26 to 40
print(f"{(fifthGroup / totalPeople) * 100:.2f}%")  # Percentage of people in groups of 41 or more
