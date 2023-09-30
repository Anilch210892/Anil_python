

with open('10_9_example.txt','r') as file:
    lines = file.readlines()
with open(r'write_output.txt', 'w+') as file_1:
    for line in lines:
        file_1.write(line)