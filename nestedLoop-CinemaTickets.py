# 6. Cinema Tickets

# Initialize counters for total tickets and ticket types
totalTickets = 0
studentTickets = 0
standardTickets = 0
kidsTickets = 0

# Infinite loop to process each movie
while True:

    # Input: Movie title
    movieTitle = input()

    # If the input is "Finish", break the loop and stop processing
    if movieTitle == "Finish":
        break

    # Input: Number of free seats available for the current movie
    freeSeats = int(input())

    # Initialize the counter for tickets sold for the current movie
    ticketsSold = 0

    # Loop to process ticket sales for the current movie until seats are filled
    while ticketsSold < freeSeats:

        # Input: Type of ticket being sold
        ticketType = input()

        # If the input is "End", stop selling tickets for this movie
        if ticketType == "End":
            break
        # If ticket is for a student, increment student ticket counter
        elif ticketType == "student":
            studentTickets += 1
        # If ticket is for a standard ticket, increment standard ticket counter
        elif ticketType == "standard":
            standardTickets += 1
        # If ticket is for a kid, increment kids ticket counter
        elif ticketType == "kid":
            kidsTickets += 1

        # Increment the total tickets sold for this movie
        ticketsSold += 1

    # Calculate the percentage of seats filled for the current movie
    percentageFull = (ticketsSold / freeSeats) * 100

    # Output the percentage of the movie theater that was filled
    print(f"{movieTitle} - {percentageFull:.2f}% full.")

# After all movies, calculate the total tickets sold
totalTickets = studentTickets + standardTickets + kidsTickets

# If there were any tickets sold, calculate and display the ticket type percentages
if totalTickets > 0:
    # Calculate percentage of student tickets
    studentPercentage = (studentTickets / totalTickets) * 100
    # Calculate percentage of standard tickets
    standardPercentage = (standardTickets / totalTickets) * 100
    # Calculate percentage of kids tickets
    kidsPercentage = (kidsTickets / totalTickets) * 100

    # Output total ticket sales and percentage breakdown by ticket type
    print(f"Total tickets: {totalTickets}")
    print(f"{studentPercentage:.2f}% student tickets.")
    print(f"{standardPercentage:.2f}% standard tickets.")
    print(f"{kidsPercentage:.2f}% kids tickets.")
