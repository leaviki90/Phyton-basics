#7.	Area of Figures
from math import pi  # Importing the value of pi for circle calculations

# Prompt the user to input the figure type: square, rectangle, circle, or triangle
figure = input("Enter the figure (square/rectangle/circle/triangle): ")

# Handling calculations for different figures based on user input
if figure == "square":
    # Square: prompt for side length and calculate the area (side * side)
    side = float(input("Enter the side length: "))
    print(round((side * side), 3))  # Output area rounded to 3 decimal places

elif figure == "rectangle":
    # Rectangle: prompt for the lengths of the two sides and calculate the area (side1 * side2)
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    print(round((side1 * side2), 3))  # Output area rounded to 3 decimal places

elif figure == "circle":
    # Circle: prompt for the radius and calculate the area (pi * radius^2)
    radius = float(input("Enter the radius: "))
    print(round((pi * radius * radius), 3))  # Output area rounded to 3 decimal places

elif figure == "triangle":
    # Triangle: prompt for the base and height, then calculate the area (0.5 * base * height)
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print(round((0.5 * base * height), 3))  # Output area rounded to 3 decimal places

else:
    # If an invalid figure is entered, display an error message
    print("Invalid figure entered.")






