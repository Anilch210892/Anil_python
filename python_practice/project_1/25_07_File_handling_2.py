"""
# # Author Anilkumar
# # problem Statement:
# # input : file handling
"""

with open('example_4.txt','r') as file:
    lines=file.readlines()
with open(r'write_output_1.txt','w+')as file_1:
    for line in lines:
        file_1.write(line)