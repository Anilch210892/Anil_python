"""Author anilkumar
problem statement:
printing even numbers and odd numbers in a particular range
"""
# num = int(input("enter the number"))  #MISTAKE
# for num in range (0,1000):
#     if num%2==0:
#         #print("The number is even number") MISTAKE
#         print(f"The number{num} is even number")
#     else:
#         print(f"The number{num} is odd number")






# expected_numbers = int(input("enter the number:"))  #for numnbers in  range of 1 to 30
# expected_range = int(input("enter the number:"))   # first 8 even numbers in range of 1 to 30
# count = 0
# for num in range (0,expected_range+1):
#     if num%2==0:
#         #print("The number is even number") MISTAKE
#         print(f"The number {num} is even number")
#         count = count+1
#         if count==8:
#             break
#     else:
#         print(f"The number {num} is odd number")



# expected_number_limit= int(input("Enter the expected_number_limit:"))  #for numnbers in  range of 1 to 30
# expected_count = int(input("Enter the expected_count:"))   # first 8 even numbers in range of 1 to 30
# count = 0
# for num in range (0,expected_number_limit+1):
#     if num%2==0:
#         print(f"The number {num} is even number")
#         count = count+1
#         if count==expected_count:
#             break
#     else:
#         print(f"The number {num} is odd number")
#
#
# expected_number_limit= int(input("Enter the expected_number_limit:"))
# expected_count = int(input("Enter the expected_count:"))
# list_1 = []
# count = 0
# for num in range (0,expected_number_limit+1):
#     if num%2==0:
#         count = count+1
#         if count==expected_count:
#             break
#         list_1.append(num)
#     else:
#         continue
#
# print(f"Total expected even numbers : {list_1}")
#

# Anil19@@@ - one value missing
expected_number_limit=int(input("Enter the expected_number_limit:"))
expected_count=int(input("Enter the expected_count"))
list_1=[]
count=0
for num in range(0,expected_number_limit+1):
    if num%2==0:
        count=count+1
        if count==expected_count:
            break
        list_1.append(num)
    else:
            continue
    print(f"the expected even numbers{list_1}")











