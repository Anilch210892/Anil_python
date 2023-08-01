
# is almost equal to ==

if 9==9:
    print("hello3")
else:
    print("hello4")

if 9 is 9:
    print("hello6")
else:
    print("hello7")
print("dummy statement")

# for more readability
def function_1():
    print("hello")

# if a function don't return anything then the value is None
if function_1() is None:
    print("function returns None")

print("To check type of the variable")
print(type(9) is int)
print(type(9) is str)