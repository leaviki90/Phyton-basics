# 5. Cake

# Input dimensions of the cake
cakeWidth = int(input("Enter the cake width: "))
cakeLength = int(input("Enter the cake length: "))

count = 0  # Initialize the counter for eaten pieces

# Calculate the total number of cake pieces
cake = cakeWidth * cakeLength

while True:
    # Prompt the user to enter the number of pieces eaten or 'STOP' to finish
    pieceOfCake = input("Enter the number of pieces eaten (or 'STOP' to finish): ")

    if pieceOfCake == "STOP":
        # If user enters 'STOP', check if there are pieces left
        if count < cake:
            remainingPieces = cake - count
            print(f"{remainingPieces} pieces are left.")
        else:
            # If no more cake is left, congratulate
            print("No more cake left! Good job!")
        break  # Exit the loop

    # Convert the input to an integer (since it's not 'STOP')
    pieceOfCake = int(pieceOfCake)
    count += pieceOfCake  # Add the eaten pieces to the total count

    # Check if the number of eaten pieces reaches or exceeds the total cake pieces
    if count < cake:
        # If there are still pieces left, continue the loop
        continue
    else:
        # If the total eaten pieces exceed the cake, calculate the excess
        excess = count - cake
        print(f"No more cake left! You need {excess} pieces more.")
        break  # Exit the loop since the cake is finished
