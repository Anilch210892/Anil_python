# Input string
input_string = "India is my country and all Indians are my brothers and sisters and one of my friend name is" \
               "@34!@%98r , it's a funny name !! right?? :)"

# Create an empty dictionary to store letter counts
letter_counts = {}

"""

{'r':[17,36,40,43,53],
'n':[15,20,31]
'd':[3,24,55]
"""
for char in input_string:
    letter_counts[char] = []

print(letter_counts)


# Iterate through the input_string[index]acters in the string
for index in range(len(input_string)):
    if input_string[index].isalpha():
        if input_string[index] in letter_counts:
            letter_counts[input_string[index]].append(index)
    elif input_string[index].isdigit():
        if input_string[index] in letter_counts:
            letter_counts[input_string[index]].append(index)
    elif  not (input_string[index].isalpha() or input_string[index].isdigit() or input_string[index] == ' '):
        letter_counts[input_string[index]].append(index)
    elif input_string[index] == ' ':
        letter_counts[input_string[index]].append(index)


print(letter_counts)