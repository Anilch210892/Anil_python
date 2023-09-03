""" Author Anilkumar
# # # problem Statement:
# # # input :list steps
# # output:
#  """
"""

str_3= input("Enter the input string:")
len_string = len(str_3)
for index in range(len_string//2):
    if str_3[index]==str_3[len(str_3)-index-1]:
        continue
    else:
        print("string is not palindrome")
        break
else:
    print("string is palindrome")

"""
str_1=input("Enter the input string:")
len_string=len(str_1)
for index in range(len_string//2):
    if str_1[index]==str_1[len(str_1)-index-1]:
        continue
    else:
        print("The input string is not palindrome")
        break
else:
    print("The input string is palindrome")















