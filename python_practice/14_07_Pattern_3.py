



for row in range(5):
    for coloumn in range(5):
        if row>coloumn:
            print("  ", end="")
        else:
            print("* ", end="")

    print()
