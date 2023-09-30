


# Input string
input_string = "this is calsoft interview"

list_1=input_string.split()
print(list_1)
list_2=list_1.reverse()
print(list_2)


"""

# Split the input string into words
words = input_string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words to form the output string
output_string = ' '.join(reversed_words)

# Print the output
print(output_string)
"""





for row in range(5):
    for column in range(row+1):
        print("*", end=" ")
    print()

print("---------------------------------------------------------------------------------------")

for row in range(5, -1, -1):
    for column in range(row):
        print("*", end=" ")
    print()

print("---------------------------------------------------------------------------------------")
for row in range(8):
    if row % 2 == 0:
        for column in range(row+1):
            print("*", end=" ")
        print()

print("---------------------------------------------------------------------------------------")

for row in range(8, -1, -1):
    if row % 2 == 0:
        for column in range(row-1):
            print("*", end=" ")
        print()





