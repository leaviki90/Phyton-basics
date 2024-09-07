#petstore task
while True:
    try:
        # Prompt the user to input the number of dog food packs and convert it to an integer
        dogFoodPack = int(input())
        # Prompt the user to input the number of cat food packs and convert it to an integer
        catFoodPack = int(input())

        # Check if both values are within the valid range (0 to 100)
        if 0 <= dogFoodPack <= 100 and 0 <= catFoodPack <= 100:
            # Calculate the total price based on the given rates
            endSum = dogFoodPack * 2.5 + catFoodPack * 4

            # Print the calculated sum with the currency in USD
            print(f"{endSum} USD.")

            # Exit the loop once the valid input is provided
            break
        else:
            # Inform the user that the input values should be between 0 and 100
            print("Please, enter the value between 0 and 100")

    # Handle the case when the user enters non-integer values
    except ValueError:
        print("Input has to be an integer")
