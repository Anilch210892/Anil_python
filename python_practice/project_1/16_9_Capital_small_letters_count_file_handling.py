
with open('16_9_file_practice.txt','r') as file:
    lines=file.readlines()
with open(r'16_9_output.txt','w+')as file_1:
    for line in lines:
        file_1.write(line)