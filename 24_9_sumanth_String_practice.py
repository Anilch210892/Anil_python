

"""
input_string="anil kumar is a software engineer"

a postion is odd then print that word
if a position is even position then word is not printed

"""
list_1=[]
input_string="anil kumar is a software engineer"
list_1 = input_string.split()
print(list_1)
for index in range(len(list_1)):
    if len(list_1[index])%2==1:
        print(list_1)
    pass

















































