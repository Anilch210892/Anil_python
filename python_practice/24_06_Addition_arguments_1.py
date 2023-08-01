# """
# Author:Anilkumar
# problem statement: printing arguments function values
# input : a,b
# output :
# """

def addition(*args):
    sum_1=0
    for element in args:
        sum_1=sum_1+element
    return sum_1
varible_1=addition(2,6,8)
varible_2=addition(3,5,1,6)
varible_3=addition()
varible_4=addition(2,6,7,9,-6,-4,5)

print(f"The value of varible_1 is {varible_1}")
print(f"The value of varible_2 is {varible_2}")
print(f"The value of varible_3 is {varible_3}")
print(f"The value of varible_4 is {varible_4}")















