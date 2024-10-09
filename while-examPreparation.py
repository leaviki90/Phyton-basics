# 2. Exam Preparation

# Prompt the user to enter the number of allowed poor grades
poorGradesNum = int(input("Enter the number of allowed poor grades: "))
# Initialize a counter for bad grades
badGradesCounter = 0
# Initialize the sum of all grades
gradesSum = 0
# Initialize the total number of problems attempted
allProbNumbs = 0
# Initialize the name of the last problem entered
lastProbName = ""

# Start an infinite loop to process each problem
while True:
    # Read problem name first to handle "Enough"
    probName = input("Enter the name of the problem (or 'Enough' to stop): ")

    # Check if the user wants to stop entering problems
    if probName == "Enough":
        if allProbNumbs > 0:
            # Calculate the average score
            averageScore = gradesSum / allProbNumbs
            print(f"Average score: {averageScore:.2f}")
            print(f"Number of problems: {allProbNumbs}")
            print(f"Last problem: {lastProbName}")
        else:
            # Inform the user that no problems were entered
            print("No problems were entered.")
        # Exit the loop since the user has finished entering data
        break

    # Read the grade for the current problem
    grade = int(input(f"Enter the grade for {probName}: "))
    # Update the name of the last problem
    lastProbName = probName
    # Increment the total number of problems attempted
    allProbNumbs += 1
    # Add the current grade to the total sum of grades
    gradesSum += grade

    # Check if the entered grade is poor (4 or below)
    if grade <= 4:
        # Increment the counter for bad grades
        badGradesCounter += 1
        # If the number of consecutive poor grades reaches the allowed limit
        if badGradesCounter == poorGradesNum:
            print(f"You need a break, {poorGradesNum} poor grades.")
            # Exit the loop as the user has exceeded the allowed number of poor grades
            break
    else:
        # Reset the bad grades counter if a good grade is entered
        badGradesCounter = 0
