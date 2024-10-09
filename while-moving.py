# 7.	Moving
# Read dimensions of the free space
freeSpaceWidth = int(input("Enter the width of the free space: "))
freeSpaceLength = int(input("Enter the length of the free space: "))
freeSpaceHeight = int(input("Enter the height of the free space: "))

# Calculate total available space in cubic meters
freeSpaceAvailable = freeSpaceWidth * freeSpaceLength * freeSpaceHeight

# Continue looping until "Done" is entered
while True:
    boxes = input("Enter the number of boxes (or 'Done' if finished): ")

    if boxes == "Done":
        # If there's still space left when done
        print(f"{freeSpaceAvailable} Cubic meters left.")
        break

    # Convert input to integer since it's not "Done"
    boxes = int(boxes)

    # Subtract the number of boxes from the available free space
    freeSpaceAvailable -= boxes

    # Check if free space has run out
    if freeSpaceAvailable < 0:
        print(
            f"No more free space! You need {abs(freeSpaceAvailable)} Cubic meters more."
        )
        break
