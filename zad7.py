
#a = 24/9;
#print(a); #daje tacan rezultat

#b = 24 //9; #najveci ceo broj
#print(b);

#c = 24 % 9; #daje ostatak pri deljenju
#print(c);

#nije dozvoljeno deljenje nulom
#7, 8, 9 za domaći

architectName = input();

# Infinite loop that keeps asking for a valid number of projects
while True:
    try:
        # Prompting the user to enter an integer
        numberOfProjects = int(input());

        # Check if the entered number is within the valid range
        if 0 <= numberOfProjects <= 100:
            break;  # Exit the loop if the number is valid
        else:
            # Inform the user if the number is out of the valid range
            print("Number should be between 0 and 100.");

    # Handle the case where the input is not a valid integer (string, special character, etc).
    except ValueError:
        print("Input should be an integer");

# Calculate the total hours needed based on the number of projects
hoursPerProject = numberOfProjects * 3;

# Display the final output with the architect's name and calculated hours
print(f"The architect {architectName} will need {hoursPerProject} hours to complete {numberOfProjects} project/s.");
