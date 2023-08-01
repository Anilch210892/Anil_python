from math import pi
print(f"The bulitin of pi is {pi}")
pi=4.26
print(f"The global  of pi is {pi}")
def outer_function():
    pi=5.26
    print(f"The enclose of pi is {pi}")
    def local_function():
        nonlocal pi
        pi = 6.89
        print(f"The local of pi is {pi}")
    local_function()
    print(f"The enclose2 of pi is {pi}")
outer_function()