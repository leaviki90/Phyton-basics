# 9. Fish Tank

# Reads the length, width, and height of the fish tank in centimeters. Converts input to integers.
lengthCm = int(input())
widthCm = int(input())
heightCm = int(input())

# Reads the percentage of the tank that will not be filled with water (e.g., space taken by decorations, air, etc.). Converts input to a float.
percentage = float(input())

# Calculate the total volume of the tank in cubic centimeters, then divide by 1000 to convert it to liters.
volume = (lengthCm * widthCm * heightCm) / 1000  # Convert cubic centimeters to liters

# Calculate the percentage of the tank that will be filled with water.
percentageWater = 100 - percentage  # Calculate the percentage of the tank that will be filled with water

# Calculate the volume of water that will fill the tank, based on the percentage of space available for water.
waterNeeded = (percentageWater / 100) * volume

# Print the amount of water needed in liters.
print(waterNeeded)
