


# Input string
input_string = "India is my country and all Indians are my brothers and sisters"

# Create a dictionary to store the occurrences of each letter along with their positions
letter_occurrences = {}

# Remove spaces and convert the input string to lowercase
input_string = input_string.replace(" ", "").lower()

# Iterate through the characters in the string
for index, char in enumerate(input_string):
    if char.isalpha():  # Check if the character is a letter
        if char in letter_occurrences:
            letter_occurrences[char].append(index)  # Append the position to the existing list
        else:
            letter_occurrences[char] = [index]  # Create a new list for the letter if it's not in the dictionary

# Print the letter occurrences
for letter, positions in letter_occurrences.items():
    print(f"'{letter}': {positions}")

# Example of how to check the occurrences of a specific letter, e.g., 'i'
letter_to_check = 'i'
if letter_to_check in letter_occurrences:
    print(f"The occurrences of '{letter_to_check}' are at positions: {letter_occurrences[letter_to_check]}")
else:
    print(f"'{letter_to_check}' is not present in the string.")
