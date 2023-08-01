"""
# Author:Anilkumar
# problem statement: printing arguments function values
# input : a,b
# output :
# """



a = int(input("Enter the values of a"))
b = int(input("Enter the values of b"))
def add(a,b):
    return a+b
c = add(a,b)
print(f"The value of c is {c}")



e = int(input("Enter the values of e"))
f = int(input("Enter the values of f"))
g = int(input("Enter the values of g"))
h = int(input("Enter the values of h"))
def add(e,f,g,h):
    return e+f+g+h
d = add(e,f,g,h)
print(f"The value of d is {d}")