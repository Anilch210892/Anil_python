"""
Author anilkumar
problem statement:
caliculator program
Here we are having 2 varibles and 5 functions.They are addition,subtraction,multiplication,division and modulus
"""
varible_1 = float(input("enter the values of varible_1"))
varible_2 = float(input("enter the values of  varible_2"))
expression = input("enter expresion")

def add(varible_1,varible_2):
    return varible_1+varible_2
def sub(varible_1,varible_2):
    return varible_1-varible_2
def mul(varible_1,varible_2):
    return varible_1*varible_2
def div(varible_1,varible_2):
    return varible_1/varible_2
def reminder(varible_1,varible_2):
    return varible_1%varible_2

if expression == 'a':
    result = add(varible_1,varible_2)
elif expression == 's':
    result = sub(varible_1,varible_2)
elif expression == 'm':
    result = mul(varible_1,varible_2)
elif expression == 'd':
    result = div(varible_1,varible_2)
elif expression == 'r':
    result= reminder(varible_1,varible_2)
else:
    print("Invalid operation")

dictionary_1={"a":"addition",
              "b":"subtraction",
              "c":"multiplication",
              "d":"division",
              "e":"reminder"}
print(f"values passed are {varible_1} and  {varible_2}")
print(f"Selected operation is {dictionary_1[expression]} and result is {result}")


