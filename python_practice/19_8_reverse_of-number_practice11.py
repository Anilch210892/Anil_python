


num = int(input("Enter the number"))
print(str(num)[::-1])









"""
num = int(input("Enter the number"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Reversed Number is: " , reversed_num)

"""









"""
# Program to reverse the digits of a number literally
# Input  = 1234
# Output = 4321


num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    rem = num % 10                  # extract the last digit
    reverse = reverse * 10 + rem    # append rem to the end of the reversed number
    num //= 10                      # drop the last digit

print("Reversed number: ", reverse)
"""

















