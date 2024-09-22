# On Time for the Exam Calculator

# Get the exam time (hour and minute) from user input
examHour = int(input("Enter exam hour: "))
examMinute = int(input("Enter exam minute: "))

# Get the arrival time (hour and minute) from user input
arrivalHour = int(input("Enter arrival hour: "))
arrivalMinute = int(input("Enter arrival minute: "))

# Convert exam and arrival times to total minutes from the start of the day
examTimeInMinutes = examHour * 60 + examMinute
arrivalTimeInMinutes = arrivalHour * 60 + arrivalMinute

# Calculate the difference in minutes between arrival time and exam time
timeDifference = arrivalTimeInMinutes - examTimeInMinutes

# Determine if the student is late, on time, or early
if timeDifference > 0:
    print("Late")  # Arrival is after the exam start
    if timeDifference >= 60:
        # Calculate hours and minutes late if the difference is 60 minutes or more
        hoursLate = timeDifference // 60
        minutesLate = timeDifference % 60
        print(f"{hoursLate}:{minutesLate:02d} hours after the start")
    else:
        # Output minutes late if less than 60 minutes
        print(f"{timeDifference} minutes after the start")
elif -30 <= timeDifference <= 0:
    print("On time")  # Arrival is within 30 minutes before the exam
    if timeDifference < 0:
        # Output minutes early if within the "on time" window
        print(f"{-timeDifference} minutes before the start")
else:
    print("Early")  # Arrival is more than 30 minutes before the exam
    if timeDifference <= -60:
        # Calculate hours and minutes early if the difference is 60 minutes or more
        hoursEarly = abs(timeDifference) // 60
        minutesEarly = abs(timeDifference) % 60
        print(f"{hoursEarly}:{minutesEarly:02d} hours before the start")
    else:
        # Output minutes early if less than 60 minutes
        print(f"{-timeDifference} minutes before the start")
