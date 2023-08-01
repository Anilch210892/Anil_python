
# """
# Author anilkumar
# problem statement:
# input : Ages of 5 persons,Heights of 5 persons and Names of 5 persons
# output: "Raviteja":29

# """
####
list_2=[29,33,32,34,28,5.7,5.9,5.6,5.10,5.8,"Raviteja","Vamsi","Vinay","Anil","Kartik"]
dict_3={}
for index in range(0,5):
    dict_3[list_2[index+10]]=list_2[index]

print(dict_3)
