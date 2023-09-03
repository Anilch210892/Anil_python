

input_number=int(input("Enter the number to be checked:"))
for number in range(2,input_number):
    if input_number%number==0:
        print(f"The number is not a prime number,input number {input_number} divided by {number}")
        pass
else:
    print(f"The input_number {input_number} a prime number")
