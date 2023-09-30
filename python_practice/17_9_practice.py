


# Input string
input_string = "India is my country and all Indians are my brothers and sisters"

# Create an empty dictionary to store letter counts
letter_counts = {}

# Remove spaces and convert the input string to lowercase
input_string = input_string.replace(" ", "").lower()

# Iterate through the characters in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in letter_counts:
            letter_counts[char] += 1  # Increment the count if it's already in the dictionary
        else:
            letter_counts[char] = 1  # Add the letter to the dictionary if it's not there

# Print the total number of letters in the string
total_letters = sum(letter_counts.values())
print(f"Total letters in the string: {total_letters}")

# Print the letter counts
for letter, count in letter_counts.items():
    print(f"'{letter}': {count}")

# Example of how to check the count of a specific letter, e.g., 'i'
letter_to_check = 'i'
if letter_to_check in letter_counts:
    print(f"The count of '{letter_to_check}' is: {letter_counts[letter_to_check]}")
else:
    print(f"'{letter_to_check}' is not present in the string.")
