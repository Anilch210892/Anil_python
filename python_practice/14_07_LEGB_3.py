from math import pi
print(f"The bulitin of pi is {pi}")
pi=4.26
print(f"The global  of pi is {pi}")
def outer_function():
    pi=5.26
    print(f"The enclose of pi is {pi}")
    def local_function():
        pi=6.86
        print(f"The local of pi is {pi}")
    local_function()
outer_function()