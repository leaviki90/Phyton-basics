# Summer Outfit Suggestion

# Input the temperature in degrees and time of the day
degrees = int(input("Enter the temperature in degrees: "))
timeOfTheDay = input("Enter the time of the day (Morning, Afternoon, Evening): ")

# Initialize outfit and shoes variables
outfit = ""
shoes = ""

# Determine outfit and shoes based on the temperature and time of the day
if timeOfTheDay == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif timeOfTheDay == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif timeOfTheDay == "Evening":
    # The evening outfit and shoes are the same regardless of the temperature
    outfit = "Shirt"
    shoes = "Moccasins"

# Output the selected outfit and shoes
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
