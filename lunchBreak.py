#8. Lunch Break
import math  # Importing the math module to use the ceil function

# Prompt user for the series name, episode duration, and break duration
seriesName = input("Enter the name of the series: ")  # The name of the series
episodeDuration = int(input("Enter the duration of the episode (10-90 minutes): "))  # Episode duration (integer in range [10…90])
breakDuration = int(input("Enter the duration of your break (10-120 minutes): "))  # Break duration (integer in range [10…120])

# Define the percentage of the break used for lunch and rest
lunchTime = 0.25  # 25% of the break time is used for lunch
uninterruptedRest = 1 / 8  # 1/8th (12.5%) of the break is uninterrupted rest

# Calculate the remaining time after lunch and rest
breakDurationLeft = breakDuration - (breakDuration * lunchTime) - (breakDuration * uninterruptedRest)

# Check if there is enough time left to watch the entire episode
if breakDurationLeft >= episodeDuration:
    # If there is enough time, calculate and print the remaining free time after watching the episode
    freeTime = math.ceil(breakDurationLeft - episodeDuration)  # Rounds up to the nearest whole number
    print(f"You have enough time to watch {seriesName} and will have {freeTime} minutes of free time left.")
else:
    # If there isn't enough time, calculate and print how many more minutes are needed to finish the episode
    additionalTimeNeeded = math.ceil(episodeDuration - breakDurationLeft)  # Rounds up to the nearest whole number
    print(f"You don't have enough time to watch {seriesName}, you need {additionalTimeNeeded} more minutes.")
