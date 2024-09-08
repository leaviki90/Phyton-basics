# 8. Basketball Equipment

# Reads the annual training fee and converts it to an integer.
annualFee = int(input())

# Calculates the price of the sneakers, which is 40% less than the annual fee.
sneakers = annualFee * 60 / 100  # Sneakers cost 60% of the annual fee

# Calculates the price of the outfit, which is 20% cheaper than the sneakers.
outfit = sneakers * 80 / 100  # Outfit costs 80% of the price of the sneakers

# Calculates the price of the basketball, which is 1/4 of the price of the outfit.
ball = outfit * 0.25  # Ball costs 25% of the price of the outfit

# Calculates the price of the accessories, which is 1/5 of the price of the ball.
accessories = ball * 0.2  # Accessories cost 20% of the price of the ball

# Calculates the total fee, which includes the annual fee, sneakers, outfit, ball, and accessories.
totalFee = annualFee + sneakers + outfit + ball + accessories

# Prints the total fee, which is the sum of all the calculated costs.
print(totalFee)
