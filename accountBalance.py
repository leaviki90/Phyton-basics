# 5.	Account Balance
linie = ""  # Initialize the variable to store the input
sum1 = 0  # Initialize the sum to 0

while True:
    linie = input()  # Read input from the user
    if linie == "NoMoreMoney":  # Break the loop if the user enters "NoMoreMoney"
        break

    try:
        linie = float(linie)  # Try to convert the input to a float
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue  # Skip to the next iteration if the input is not a valid number

    if linie < 0:  # If the input is negative, show an error and stop the loop
        print("Invalid operation!")
        break

    print(f"Increase: {linie:.2f}")  # Print the increase with two decimal places
    sum1 += linie  # Add the current input to the sum

print(f"Total: {sum1:.2f}")  # Print the total sum after the loop ends
