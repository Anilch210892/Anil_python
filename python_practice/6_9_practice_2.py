

"""
P.s : getting sqaure and cube of numbers
input: True. 2,3
output : 4,27
input: False. 2,3
output : 8,9

"""
def func_1(flag,var_1,var_2):
    if flag=="T":
        return var_1**2,var_2**3
    else:
        return var_1**3,var_2**2
flag,var_1,var_2=input("Enter the 3 variables: ").split()
# for splitting more number of variables into single variables  we will use split
# We are assigning multiple values in 1 statement is known as unpacking
# ValueError: not enough values to unpack (expected 3, got 2)
var_1=int(var_1)
var_2=int(var_2)
output_1,output_2=func_1(flag,var_1,var_2)
print(f"output_1:{output_1},output_2:{output_2}")













