# """
# Author anilkumar
# problem statement:
# caliculator program
# """
#
# a=int(input("enter the values of a"))
# b=int(input("enter the values of b"))
# def add(a,b):
#     return a+b
# c=add(a,b)
# print(c)
#
# e=int(input("enter the values of e"))
# f=int(input("enter the values of f"))
# g=int(input("enter the values of g"))
# h=int(input("enter the values of h"))
# def add(e,f,g,h):
#     return e+f+g+h
# d=add(e,f,g,h)
# print(d)
#
#

def addition(*args):
    sum_1=0
    for element in args:
        sum_1=sum_1+element
    return sum_1
varible_1=addition(2,6,8)
varible_2=addition(3,5,1,6)
varible_3=addition()
varible_4=addition(2,6,7,9,-6,-4,5)

print(varible_1)
print(varible_2)
print(varible_3)
print(varible_4)















