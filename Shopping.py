#7. Shopping
# Input Section
peterBudget = float(input("Enter Peter's budget: "))  # Peter's total available budget in USD
videoCardsNum = int(input("Enter the number of video cards: "))  # Number of video cards Peter wants to buy
cpuNum = int(input("Enter the number of CPUs: "))  # Number of CPUs Peter wants to buy
ramNum = int(input("Enter the number of RAM sticks: "))  # Number of RAM sticks Peter wants to buy

# Step 1: Calculate the total cost for video cards
videoCardsCost = videoCardsNum * 250  # Each video card costs $250

# Step 2: Calculate the total cost of CPUs
# The cost of each CPU is 35% of the total price of one video card
cpuCost = (videoCardsCost * 0.35) * cpuNum

# Step 3: Calculate the total cost of RAM
# The cost of each RAM stick is 10% of the total price of one video card
ramCost = (videoCardsCost * 0.10) * ramNum

# Step 4: Calculate the total cost before any discounts
totalCost = videoCardsCost + cpuCost + ramCost  # Sum of video cards, CPUs, and RAM

# Step 5: Apply the discount if Peter buys more video cards than CPUs
if videoCardsNum > cpuNum:
    totalCost *= 0.85  # Apply a 15% discount if the condition is met

# Step 6: Compare the total cost with Peter's budget
if peterBudget >= totalCost:
    # Peter has enough money; calculate and display the leftover amount
    moneyLeft = peterBudget - totalCost
    print(f"You have {moneyLeft:.2f} USD left!")
else:
    # Peter doesn't have enough money; calculate and display the additional amount needed
    moneyNeeded = totalCost - peterBudget
    print(f"Not enough money! You need {moneyNeeded:.2f} USD more!")


