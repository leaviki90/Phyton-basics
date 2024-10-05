#7.	Min Number

n = int(input())  # Initialize 'n' as the first input
smallest = n  # Set 'smallest' to the value of 'n'

while True:
    linie = input()  # Read input as a string
    if linie == "Stop":  # If input is "Stop", exit the loop
        break

    linie = int(linie)  # Convert the input to an integer
    if linie < smallest:  # If the input is smaller than the current smallest value
        smallest = linie  # Update 'smallest' to the new smallest value

print(smallest)  # Print the smallest value found
