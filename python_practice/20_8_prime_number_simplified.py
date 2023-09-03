



input_number=int(input("Enter the input number:"))
# # if a for loop never breaks program flow, then only  enter into else part
for number in range(2,input_number):
    if input_number%number==0:
        print(f"The number is not a prime number")
        break
else:
    print(f"The input_number {input_number} is a prime number")

