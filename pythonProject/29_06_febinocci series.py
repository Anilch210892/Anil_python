
# # """
# # Author Anilkumar
# # problem statement:
# # input : printing febinocci series of first 10 numbers
# output:
# """

num_1=0
num_2=1
number_fibonacci=int(input("Enter the number_fibonacci:"))
list_1 = [num_1,num_2]
# Eg: 10  -->0,7
# 2 numbers already exists
for number in range(0,number_fibonacci-2):
    num_3 = num_1+num_2
    num_1 = num_2
    num_2 = num_3
    list_1.append(num_3)
print(f"Final list is : {list_1}")

