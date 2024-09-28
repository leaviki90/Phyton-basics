#6.	Vowels Sum
# Read a word from user input and convert it to lowercase to handle case insensitivity
word = input().lower()

# Initialize a variable to store the sum of vowels
sumOfVowels = 0

# Loop through each character in the word
for i in word:
    # Check if the character is a vowel and assign a specific value to it
    if i == "a":
        sumOfVowels += 1  # Add 1 if the vowel is 'a'
    elif i == "e":
        sumOfVowels += 2  # Add 2 if the vowel is 'e'
    elif i == "i":
        sumOfVowels += 3  # Add 3 if the vowel is 'i'
    elif i == "o":
        sumOfVowels += 4  # Add 4 if the vowel is 'o'
    elif i == "u":
        sumOfVowels += 5  # Add 5 if the vowel is 'u'

# Print the final sum of vowel values
print(sumOfVowels)
