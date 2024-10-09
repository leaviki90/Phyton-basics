# 3. Vacation

# Prompt the user to enter the amount of money Jessie needs for her vacation
moneyNeeded = float(input("Enter the amount of money needed: "))
# Prompt the user to enter the current amount of available money
availableMoney = float(input("Enter the available money: "))
# Initialize the total number of days that have passed
totalDaysPassed = 0
# Initialize a counter to track consecutive days of spending
spendCounter = 0

# Start an infinite loop to process daily actions
while True:
    # Read the action Jessie wants to perform: 'spend' or 'save'
    action = input("Enter the action ('spend' or 'save'): ")
    # Read the amount of money associated with the action
    amount = float(input("Enter the amount of money: "))
    # Increment the total number of days passed
    totalDaysPassed += 1

    if action == "spend":
        # If Jessie spends, increment the spend counter
        spendCounter += 1
        # Subtract the amount from available money, but don't let it go below 0
        availableMoney -= amount
        if availableMoney < 0:
            availableMoney = 0
        # If Jessie spends for 5 consecutive days, stop the program
        if spendCounter == 5:
            print("You can't save the money.")
            print(f"Days passed: {totalDaysPassed}")
            break

    elif action == "save":
        # Reset the spend counter since Jessie saved money today
        spendCounter = 0
        # Add the saved amount to the available money
        availableMoney += amount
        # Check if Jessie has saved enough money for the vacation
        if availableMoney >= moneyNeeded:
            print(f"You saved the money in {totalDaysPassed} days.")
            break

    else:
        # Handle invalid input if neither 'spend' nor 'save' is entered
        print("Invalid action entered. Please enter 'spend' or 'save'.")
