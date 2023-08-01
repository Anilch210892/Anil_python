
# # """
# # Author Anilkumar
# # problem statement: Program to display the Fibonacci sequence up to n-th term
# # input : printing febinocci series of first 10 numbers
# output:0,1,1,2,3,5,8,13,21,34
# """



nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto nterms:")
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
