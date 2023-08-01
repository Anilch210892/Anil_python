"""
# # Author Anilkumar
# # problem Statement: printing tables
#
"""

# start, end, step
for number in range(1,12):
    for table in range(1,11):
        print(f"{table}*{number}={table*number}",end="              ")
    print("")

