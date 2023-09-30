
def count_letters(name):
    # Remove spaces and convert the name to lowercase (if needed)
    name = name.replace(" ", "").lower()

    # Use the len() function to count the number of letters
    letter_count = len(name)

    return letter_count

# Get the name from the user
name = input("Enter a name: ")

# Call the function to count the letters in the name
result = count_letters(name)

# Display the result
print(f"The name '{name}' contains {result} letters.")
