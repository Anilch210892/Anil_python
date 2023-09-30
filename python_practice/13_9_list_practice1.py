
"""


list_1=[1,6,9,14,26,"Raviteja","Anil","Vinay",8.9,10.6,"A",56]
print(list_1)
for index in range(len(list_1)):
    print(f" In index {index} element is {list_1[index]}")




print("-----------------------------------------------------------------------")



"""




#for replacing  index 0 as  100, 1 as 101, 2 as 102...... we should add {index+100}

"""  
      
for index in range(len(list_1)):
    print(f" In index {index+100} element is {list_1[index]}")
   
   
print("-----------------------------------------------------------------------")     
    
"""




# input - list_1=[1,6,9,14,26,"Raviteja","Anil","Vinay",8.9,10.6,"A",56]
# output - list_1=[101,106,109,114,126,"Raviteja","Anil","Vinay",108.9,110.6,"A",156]


"""  

list_1=[1,6,9,14,26,"Raviteja","Anil","Vinay",8.9,10.6,"A",56]
for index in range(len(list_1)):
    if type(list_1[index]) is str:
        list_1[index] = list_1[index]+"hi"
        print(f" In index {index} element is {list_1[index]}")

    elif type(list_1[index]) is int:
        print(f" In index {index} element is {list_1[index]+100}")

    elif  type(list_1[index]) is float:
        print(f" In index {index} element is {list_1[index]+51.4}")

"""



list_1=[1,6,9,14,26,"Raviteja","Anil","Vinay",8.9,10.6,"A",56]

# 2nd table
#for index in range (len(list_1) , WHEN INDEX STARTS FROM 1  WE MUST ADD +1,  (1,LEN(LIST_1)+1)

for index in range(0,len(list_1)):
    if index%2==0:
        print(f" In index {index} element is {list_1[index]}")

print("-----------------------------------------------------------------------")





for index in range(0,len(list_1)):
    if index % 3 != 0:
        print(f" In index {index} element is {list_1[index]}")































