"""
# # Author Anilkumar
# # problem Statement:
# # input : scope practice
"""

PI = 3.14
print(f"starting global value is {PI}")
def outer_function():
    # print(f"the outer_function{PI}")
    # UnboundLocalError: cannot access local variable 'PI' where it is not associated with a value
    PI = 3.156
    print(f"the outer_function{PI}")
    def inner_function():
        PI = 3.815
        print(f"the inner_function{PI}")
    inner_function()
outer_function()
print(f"ending global value is {PI}")




