# 4. Walking

count = 0  # Initialize the step counter to zero, to keep track of the total steps Emma has walked.

# Start an infinite loop to continuously ask for steps until a condition is met to stop.
while True:
    # Prompt the user to enter the number of steps or the command "Going home".
    steps = input("Enter the number of steps (or 'Going home'): ")

    # Check if Emma decided to go home by entering the command "Going home".
    if steps == "Going home":
        # Emma is heading home, so we now ask her how many more steps she walked while going home.
        remainSteps = int(input("Enter the remaining steps after going home: "))
        # Add these remaining steps to the total count.
        count += remainSteps

        # After going home, check if Emma has reached or exceeded her goal of 10,000 steps.
        if count < 10000:
            # If Emma hasn't reached the goal yet, calculate how many steps she still needs.
            print(f"{10000 - count} more steps to reach the goal.")
        else:
            # If Emma has reached or exceeded the goal, print a success message.
            print("Goal reached! Good job!")
            # Calculate and print how many steps she walked beyond the goal.
            print(f"{count - 10000} steps over the goal!")
        # Break the loop since Emma is done walking for the day.
        break

    else:
        # If the user didn't input "Going home", assume the input is a number of steps.
        # Convert the input (which is a string) to an integer so it can be used in calculations.
        steps = int(steps)
        # Add the entered steps to the total count of steps Emma has walked so far.
        count += steps

        # Check if the total steps count has reached or exceeded the goal of 10,000 steps.
        if count >= 10000:
            # If Emma has reached or exceeded the goal, print a success message.
            print("Goal reached! Good job!")
            # Calculate and print how many steps she walked beyond the goal.
            print(f"{count - 10000} steps over the goal!")
            # Break the loop since Emma has met her goal.
            break
