#5.	Character Sequence
# Take user input and store it in the variable 'someText'
someText = input()

# This is an alternative approach to determine the length of the string
# lengthOfSomeText = len(someText)

# First way to loop through each character by index using the length of the text
# for i in range(0, lengthOfSomeText):
#    print(someText[i])

# Second way to loop through using the length directly in the for loop
# for i in range(0, len(someText)):
#    print(someText[i])

# Third and most common way to loop through each character directly
# Here, 'i' takes each character in the string one by one
for i in someText:
    print(i)  # Print each character
