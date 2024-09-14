# 4. Vacation Books List

# Reads the total number of pages in the book and converts it to an integer.
pageNumbers = int(input())

# Reads the number of pages the user can read in one hour and converts it to an integer.
pagesInHour = int(input())

# Reads the number of days the user has to finish the book and converts it to an integer.
numberOfDays = int(input())

# Calculates the total number of hours needed to read the book by dividing the total pages by pages read per hour.
totalHours = pageNumbers // pagesInHour  # Uses integer division to get the total hours needed

# Calculates and prints the number of hours the user needs to read each day to finish the book on time.
print(totalHours // numberOfDays)  # Uses integer division to distribute the total hours over the given days
