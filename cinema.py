# Cinema Revenue Calculator

# Input the type of projection, number of rows, and number of columns (seats)
projectionType = input("Enter the projection type (Premiere, Normal, Discount): ")
rowNumber = int(input("Enter the number of rows: "))
colNumber = int(input("Enter the number of columns: "))

# Calculate the total ticket revenue based on the projection type
if projectionType == "Premiere":
    # Premiere tickets are $12 per seat
    print(f"{(rowNumber * colNumber * 12):.2f} USD")
elif projectionType == "Normal":
    # Normal tickets are $7.50 per seat
    print(f"{(rowNumber * colNumber * 7.5):.2f} USD")
elif projectionType == "Discount":
    # Discount tickets are $5 per seat
    print(f"{(rowNumber * colNumber * 5):.2f} USD")
else:
    # Handle invalid projection type input
    print("Error: Invalid projection type")
