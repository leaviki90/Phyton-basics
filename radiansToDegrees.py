#2.	Convertor: from radians to degrees
from math import pi  # Imports the constant pi from the math module

# 2. Converter: from radians to degrees

# Reads the angle in radians from the user and converts it to a float to allow for decimal values.
radians = float(input())

# Converts the angle from radians to degrees using the formula: degrees = radians * 180 / pi
angle = radians * 180 / pi

# Prints the converted angle in degrees.
print(angle)


