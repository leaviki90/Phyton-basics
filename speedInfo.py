#6.	Speed Info
# Prompt the user to input the speed as a floating-point number
speed = float(input())

# Determine and print the speed category based on the input
if speed <= 10:
    # Speeds less than or equal to 10 are considered "slow"
    print("slow")
elif speed <= 50:
    # Speeds between 11 and 50 (inclusive) are categorized as "average"
    print("average")
elif speed <= 150:
    # Speeds between 51 and 150 (inclusive) are categorized as "fast"
    print("fast")
elif speed <= 1000:
    # Speeds between 151 and 1000 (inclusive) are considered "ultra fast"
    print("ultra fast")
else:
    # Any speed above 1000 is categorized as "extremely fast"
    print("extremely fast")

