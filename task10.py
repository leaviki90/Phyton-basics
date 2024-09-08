# 1. Converter: from USD to BGN

# Reads the amount in USD from the user and converts it to a float to allow for decimal values.
dollar = float(input())

# Converts the amount from USD to BGN using the fixed exchange rate (1 USD = 1.79549 BGN).
bgn = dollar * 1.79549

# Prints the converted amount in BGN.
print(bgn)

