#4.	Personal Titles
# Get the user's age as a float (to account for non-integer input)
age = float(input("Enter your age: "))

# Get the user's gender as input ("m" for male, "f" for female)
gender = input("Enter your gender (m/f): ")

# Check if the gender is male ("m")
if gender == "m":
    # If age is 16 or older, print "Mr."
    if age >= 16:
        print("Mr.")
    # If age is less than 16, print "Master"
    else:
        print("Master")

# Check if the gender is female ("f")
elif gender == "f":
    # If age is 16 or older, print "Ms."
    if age >= 16:
        print("Ms.")
    # If age is less than 16, print "Miss"
    else:
        print("Miss")

# If the input doesn't match "m" or "f", print an error
else:
    print("Error")

