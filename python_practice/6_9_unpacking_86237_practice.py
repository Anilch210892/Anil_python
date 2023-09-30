

"""
P.S: To print sum of digits of a number

input1: 862379
input2: 6704289

print the  difference of sums of odd alternatives
sum[6,3,9] - sum[7, 4,8]

print the sum of even alternatives sums

sum[6,0,2,9] + sum[8,2,7]



"""
list_1=[]
num=int(input("Enter the number:"))
sum_1 = 0
while num>0:
    digit=num%10
    num=num//10
    digits=list_1.append(digit)
print(f"The list_1 is: {list_1}")
# don't hardcode
# print(list_1[0:4:2])
print(list_1[0:len(list_1):1])
alternate_1 = []
alternate_1=list_1[0:len(list_1):1]
sum_1=sum(alternate_1)
print(sum_1)

#  print(sum(list_1))
 #         ^^^^^^^^^^^
# TypeError: 'int' object is not callable
#DONT CREATE VARIABLES WITH sum and len names

# print another alternative numbers





