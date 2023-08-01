"""
# # Author Anilkumar
# # problem Statement:
# # input : generators
   output :
"""

print("____________________First started_____________")


def func_1():
    return 1
    return 2
    return 3
func_1()
func_1()
func_1()
func_1()
print( f"The value of func_1() is {func_1()}")
print( f"The value of func_1() is {func_1()}")
print( f"The value of func_1() is {func_1()}")


print("____________________First ended_____________")






print("____________________second started_____________")

def func_2():
    yield 1
    yield 2
    yield 3

generator = func_2()

print( f"The next yield of func_2() is {next(generator)}")
print( f"The yield of func_2() is {next(generator)}")
print( f"The yield of func_2() is {next(generator)}")

#print( f"The yield of func_2() is {next(generator)}")

#StopIteration

print( f"The yield of func_2() is {next(generator)}")

print("____________________second ended_____________")

