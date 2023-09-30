
""" Author Anilkumar
# # # problem Statement:
# # # input :Reversal of number
 # output:
#  """





letters ="ABCDEF"
letters_1=letters[::-1]
print(letters_1)



"""


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The string is : ", end="")
print(reverse(s))

"""






