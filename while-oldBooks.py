#1.	Old Books
# Input the name of the book to search for
theBook = input("Enter the name of the book you are searching for: ")
count = 0
while True:
    # Input the name of the current book being checked
    bookNames = input("Enter the name of the current book (or 'No More Books' to stop searching): ")

    # Check if the user wants to stop the search
    if bookNames == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break  # Don't forget to break out of the loop if no more books

    # If the current book matches the searched book
    if bookNames == theBook:
        print(f"You checked {count} books and found it.")
        break

    # Increase count after checking the book
    count += 1


