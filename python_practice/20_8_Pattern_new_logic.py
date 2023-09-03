


rows=5
for row in range(1,6):
    print("* "*(row)," "*(row-1))



"""
coloumns=5
for coloumn in range(1,6):
    print(" "*(coloumn)," "*(coloumns-coloumn))
"""


def print_pattern(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)















