

name = ["anil", "ravi", "vamsi"]
aadhar = ["9586", "8525", "2145"]
gender = ["male", "male", "male"]
mapped_1 = zip(name, aadhar,gender)
print(set(mapped_1))

# unzipping values
name,aadhar,gender = zip(*mapped_1)

print("The unzipped result: \n", end="")

# printing initial lists
print(f"The name list is{name} : ")

print(f"The aadhar list is{aadhar} : ")

print(f"The gender list is{gender} : ")
