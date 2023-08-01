

# C:\Users\anilc\Desktop\python_practice\project_1\Example
with open('example_2.txt','r') as file:
    lines=file.readlines()
with open(r'write_output.txt','w+')as file_1:
    for line in lines:
        file_1.write(line)