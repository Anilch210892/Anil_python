from math import pi
print(f"The bulitin of pi is {pi}")
pi=4.26
#pi=4.26 [now pi=3.14 is overrided to 4.26]
print(f"The global  of pi is {pi}")
def outer_function():
    pi=5.26
    print(f"The enclose of pi is {pi}")
    #pi=5.26 [now pi=4.26 is overrided to 5.26]
    def local_function():
        #nonlocal pi
        global pi
        pi = 6.89
        # pi=6.89 [now pi=5.26 is overrided to 6.89]
        print(f"The local of pi is {pi}")
    local_function()
    print(f"The enclose2 of pi is {pi}")
    # beacause of nonlocal keyword encloser function pi value[5.26] is overrided with local pi value[6.89]
outer_function()
print(f"The global  of pi is {pi}")
# beacause of global keyword global pi value[4.26] is overrided with local pi value[6.89]






"""



"""







