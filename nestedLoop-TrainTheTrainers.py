# 04. Train The Trainers

# Input: Number of jury members
juryNum = int(input())

# Initialize total average grade and presentation counter
totalAverageGrade = 0.0
presentationCount = 0

# Infinite loop to process presentations until "Finish" is entered
while True:

    # Input: Name of the presentation
    presentationName = input()

    # If "Finish" is entered, break the loop and stop input
    if presentationName == "Finish":
        break

    # Increment presentation count for each new presentation
    presentationCount += 1

    # Initialize sum of grades for the current presentation
    sumGrades = 0.0

    # Loop through each jury member to collect and sum their grades
    for i in range(juryNum):
        grade = float(input())  # Input: Jury member's grade
        sumGrades += grade  # Add the grade to the sum for the current presentation

    # Calculate the average grade for the current presentation
    averageGrade = sumGrades / juryNum

    # Output the average grade for the current presentation, formatted to 2 decimal places
    print(f"{presentationName} - {averageGrade:.2f}.")

    # Add the current presentation's average grade to the total average
    totalAverageGrade += averageGrade

# After all presentations are done, check if any presentations were graded
if presentationCount > 0:
    # Calculate and print the final average grade for all presentations
    finalAverage = totalAverageGrade / presentationCount
    print(f"Student's final assessment is {finalAverage:.2f}.")
else:
    # If no presentations were graded, print an appropriate message
    print("No presentations were graded.")
