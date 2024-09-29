#4.	Clever Lily
# Input the age of the child
age = int(input())

# Input the price of the washing machine the child is saving for
washMachinePrice = float(input())

# Input the price of a single toy
toyPrice = int(input())

# Initialize variables
birthdayMoney = 10  # Initial amount of money received on even birthdays
toysCount = 0  # Counter for the number of toys received
money = 0  # Total money saved

# Loop through each birthday, from 1 to the child's current age
for i in range(1, age + 1):
    # Check if it's an even birthday
    if i % 2 == 0:
        # Add the birthday money to the total money on even birthdays
        money += birthdayMoney
        # Subtract 1 unit of money because the brother takes 1 from the gift
        money -= 1
        # Increase the birthday money for the next even birthday
        birthdayMoney += 10
    else:
        # On odd birthdays, the child receives a toy instead of money
        toysCount += 1

# Calculate the total money by adding the money received and the value of the toys (toysCount * toyPrice)
totalMoney = money + toysCount * toyPrice

# Check if the total money is enough to buy the washing machine
if totalMoney >= washMachinePrice:
    # If enough money is saved, print the remaining amount after the purchase
    print(f"Yes! {(totalMoney - washMachinePrice):.2f}")
else:
    # If not enough money is saved, print how much more is needed
    print(f"No! {(washMachinePrice - totalMoney):.2f}")

