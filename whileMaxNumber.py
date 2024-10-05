#6.	Max Number

n = int(input())  # Initialize 'n' as the first input
largest = n  # Set 'largest' to the value of 'n'

while True:
    linie = input()  # Read input as a string
    if linie == "Stop":  # If input is "Stop", exit the loop
        break

    linie = int(linie)  # Convert the input to an integer
    if linie > largest:  # If the input is larger than the current largest value
        largest = linie  # Update 'largest' to the new largest value

print(largest)  # Print the largest value found
