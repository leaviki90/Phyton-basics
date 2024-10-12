# 5.	Traveling
# This script helps plan trips by saving for different destinations.
# The user inputs a destination and the required budget, then enters savings until the budget is met.
# The loop continues until the user enters "End" as the destination.

while True:
    destination = input()  # Input: destination name
    if destination == "End":  # Check if the input is "End" to stop the loop
        break  # Exit the loop if the user wants to end the program
    minBudget = float(input())  # Input: minimum budget needed for the destination
    savings = 0.0  # Initialize the savings to zero

    # Loop until the savings reach or exceed the minimum budget
    while savings < minBudget:
        saving = float(input())  # Input: amount saved
        savings += saving  # Add the saving to the total savings

    print(f"Going to {destination}!")  # Once the budget is met, print the message
