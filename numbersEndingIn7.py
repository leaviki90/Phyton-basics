#1.	Numbers Ending in 7
# Define the upper limit of the range
n = 1000

# Loop through numbers from 1 to 1000 (inclusive)
for i in range(1, n + 1):
    # Check if the last digit of the number is 7 (i.e., the number ends with 7)
    if i % 10 == 7:
        # Print the number if the condition is met
        print(i)
