num = int(input("Enter your number"))

# To take input from the user
# num = int(input("Enter a number: "))

    # check for factors
for i in range(2, num):
    if (num % i) == 0:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
