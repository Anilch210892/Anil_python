
""" Author Anilkumar
# # # problem Statement:
# # # input :Reversal of number
 # output:
#  """



"""

letters ="ABCDEF"
letters[::-1]
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








