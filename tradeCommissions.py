# 12.	Trade Commissions
# Prompt the user to input a cityName and salesVolume
cityName = input("Please enter a city name:");
salesVolume = float(input("Please enter the sales volume:"));
# Initialize commission to 0.0
commission = 0.0

# Check if salesVolume is negative
if salesVolume < 0:
    print("error")
else:
    # Check for city "London"
    if cityName == "London":
        if 0 <= salesVolume <= 500:
            commission = salesVolume * 0.05
        elif 500 < salesVolume <= 1000:
            commission = salesVolume * 0.07
        elif 1000 < salesVolume <= 10000:
            commission = salesVolume * 0.08
        elif salesVolume > 10000:
            commission = salesVolume * 0.12

    # Check for city "Paris"
    elif cityName == "Paris":
        if 0 <= salesVolume <= 500:
            commission = salesVolume * 0.045
        elif 500 < salesVolume <= 1000:
            commission = salesVolume * 0.075
        elif 1000 < salesVolume <= 10000:
            commission = salesVolume * 0.10
        elif salesVolume > 10000:
            commission = salesVolume * 0.13

    # Check for city "Rome"
    elif cityName == "Rome":
        if 0 <= salesVolume <= 500:
            commission = salesVolume * 0.055
        elif 500 < salesVolume <= 1000:
            commission = salesVolume * 0.08
        elif 1000 < salesVolume <= 10000:
            commission = salesVolume * 0.12
        elif salesVolume > 10000:
            commission = salesVolume * 0.145

    # Check if commission was calculated (city was valid)
    if cityName in ["London", "Paris", "Rome"]:
        print(f"{commission:.2f}")  # Print commission rounded to 2 decimal places
    else:
        print("error")  # Print error if city is invalid
