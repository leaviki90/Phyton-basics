#8.	Graduation
name = input()  # Get student's name
theClass = 1  # Start with grade 1
notesNum = 0  # Number of grades entered
numOfFails = 0  # Number of times the student failed
note = 0.0
totalNote = 0.0  # To calculate the total sum of valid grades
numValidNotes = 0  # Count of valid grades (grades >= 4.00)

while True:
    if theClass > 12:  # If the student has completed all 12 grades
        print(f"{name} graduated. Average grade: {totalNote / numValidNotes:.2f}")
        break
    if numOfFails >= 2:  # If the student fails more than once
        print(f"{name} has been excluded at {theClass} grade")
        break

    note = float(input())  # Input the student's grade
    notesNum += 1

    if note < 4.00:  # If the grade is below 4, count it as a fail and continue
        numOfFails += 1
        continue

    # If the grade is valid, add it to the total and increase the class level
    totalNote += note
    numValidNotes += 1
    theClass += 1  # Move to the next grade
