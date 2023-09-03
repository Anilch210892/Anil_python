



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
