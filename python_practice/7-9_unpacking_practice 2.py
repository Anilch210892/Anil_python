
"""


input1: 862379
input2: 6704289

p.s
print the  difference of sums of odd alternatives
sum[6,3,9] - sum[7, 4,8]

print the sum of even alternatives sums

sum[6,0,2,9] + sum[8,2,7]

"""




list_1=[]
num_1=int(input("Enter the number1:"))
num_2=int(input("Enter the number2:"))
sum_1 = 0
while num_1>0:
    digit=num_1%10
    num_3=num_1//10
    digits=list_1.append(digit)
while num_2>0:
    digit=num_2%10
    num_4=num_2//10


print(f"The list_1 is: {list_1}")
# don't hardcode
# print(list_1[0:4:2])
print(list_1[0:len(list_1):1])
alternate_1 = []
alternate_2 = []
alternate_1=list_1[0:len(list_1):2]
alternate_2=list_1[1:len(list_1):1]
sum_1=sum(alternate_1)+sum(alternate_2)
print(sum_1)










