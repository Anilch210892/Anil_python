"""
# # Author Anilkumar
# # problem Statement:
# # input :Checking a number is prime number or not
# output:
 """
input_number=int(input("Enter the number to be checked:"))
# # if a for loop never breaks program flow, then only  enter into else part
for number in range(2,input_number):
    if input_number%number==0:
        print(f"The number is not a prime number,input number {input_number} divided by {number}, breaking the loop")
        break
    else:
        print(f"So far, the input_number a prime number after checked by {number}")
else:
    print(f"The input_number {input_number} a prime number")
#
#


