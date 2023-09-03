

with open('26_8_example22.txt','r') as file:
    lines=file.readlines()
with open(r'write_output2233.txt','w+')as file_1:
    for line in lines:
        file_1.write(line)
