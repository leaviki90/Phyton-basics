#2.	Password
# Prompt the user to input their username
username = input()

# Prompt the user to input their password
password = input()

# Ask the user to enter the password for verification
enteredPass = input()

# Continue asking for the password until the correct one is entered
while enteredPass != password:
    enteredPass = input()  # If the entered password is incorrect, ask again

# Once the correct password is entered, print a welcome message with the username
print(f"Welcome, {username}!")



