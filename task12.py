# 3. Deposit Calculator

# Reads the initial deposit amount from the user and converts it to a float.
depositAmount = float(input())

# Reads the deposit term (in months) from the user and converts it to an integer.
depositTerm = int(input())

# Reads the annual interest rate from the user, converts it to a float, and divides by 100 to convert the percentage to a decimal.
annualInterestRate = float(input()) / 100  # Converts percentage to a decimal

# Calculates the total amount in the account after the deposit term.
# The formula adds the initial deposit to the interest earned over the deposit term.
# The interest for each month is calculated as (depositAmount * annualInterestRate) / 12.
amount = depositAmount + depositTerm * ((depositAmount * annualInterestRate) / 12)

# Prints the total amount in the account after the deposit term.
print(amount)
