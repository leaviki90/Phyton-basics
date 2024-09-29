#3.	Histogram
# Input the number of values to process
n = int(input())

# Initialize counters for each category
p1Count = 0  # Count for numbers less than 200
p2Count = 0  # Count for numbers between 200 and 399
p3Count = 0  # Count for numbers between 400 and 599
p4Count = 0  # Count for numbers between 600 and 799
p5Count = 0  # Count for numbers 800 or more

# Loop through each number input
for i in range(0, n):
    # Input the current number
    num = int(input())

    # Classify the number into one of the categories and increment the corresponding counter
    if num < 200:
        p1Count += 1
    elif 200 <= num <= 399:
        p2Count += 1
    elif 400 <= num <= 599:
        p3Count += 1
    elif 600 <= num <= 799:
        p4Count += 1
    elif num >= 800:
        p5Count += 1

# Calculate the total count of all numbers
sum1 = p1Count + p2Count + p3Count + p4Count + p5Count

# Print the percentage of numbers in each category, rounded to two decimal places
print(f"{(p1Count * 100) / sum1:.2f}%")  # Percentage of numbers less than 200
print(f"{(p2Count * 100) / sum1:.2f}%")  # Percentage of numbers between 200 and 399
print(f"{(p3Count * 100) / sum1:.2f}%")  # Percentage of numbers between 400 and 599
print(f"{(p4Count * 100) / sum1:.2f}%")  # Percentage of numbers between 600 and 799
print(f"{(p5Count * 100) / sum1:.2f}%")  # Percentage of numbers 800 or more

