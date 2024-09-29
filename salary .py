#5.	Salary

# Input the number of tabs the user opens
tabsNumber = int(input())

# Input the user's initial salary
salary = int(input())

# Loop through each opened tab
for i in range(tabsNumber):
    # Input the website visited on the current tab
    site = input()

    # Deduct salary based on the website visited
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    # If the salary reaches 0 or below, the user loses their salary and the loop breaks
    if salary <= 0:
        print("You have lost your salary.")
        break

# If the loop finishes and the salary is still above 0, print the remaining salary
if salary > 0:
    print(salary)










