# Input string
input_string = "India is my country and all Indians are my brothers and sisters and one of my friend name is" \
               "@34!@%98r , it's a funny name !! right?? :)"

# Create an empty dictionary to store letter counts
letter_counts = {}


# Iterate through the characters in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in letter_counts:
            letter_counts[char] += 1  # Increment the count if it's already in the dictionary
        else:
            letter_counts[char] = 1  # Add the letter to the dictionary if it's not there
    elif char.isdigit():
        if char in letter_counts:
            letter_counts[char] += 1  # Increment the count if it's already in the dictionary
        else:
            letter_counts[char] = 1  # Add the letter to the dictionary if it's not there
    elif  not (char.isalpha() or char.isdigit() or char == ' '):
        if char in letter_counts:
            letter_counts[char] += 1  # Increment the count if it's already in the dictionary
        else:
            letter_counts[char] = 1  # Add the letter to the dictionary if it's not there
    elif char == ' ':
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

print(letter_counts)