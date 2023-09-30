

def count_repeated_letters(input_string):
    # Initialize an empty dictionary to store letter counts
    letter_counts = {}

    # Convert the input string to lowercase to make the counting case-insensitive
    input_string = input_string.lower()

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Increment the count for the letter in the dictionary
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Print the letter counts
    for letter, count in letter_counts.items():
        if count > 1:
            print(f"The letter '{letter}' is repeated {count} times.")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    count_repeated_letters(input_string)
