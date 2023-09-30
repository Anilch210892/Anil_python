
def func_1(flag,var_1,var_2,var_3,var_4):
    if flag=="T":
        return var_1**2,var_2**3
    else:
        return var_1**3,var_2**2
flag,var_1,var_2,var_3,var_4=input("Enter the 5 variables: ").split()
# for splitting more number of variables into single variables  we will use split
# We are assigning multiple values in 1 statement is known as unpacking
# ValueError: not enough values to unpack (expected 3, got 2)
var_1=int(var_1)
var_2=int(var_2)
var_3=int(var_3)
var_4=int(var_4)
output_1,output_2=func_1(flag,var_1,var_2)
print(f"output_1:{output_1},output_2:{output_2}")