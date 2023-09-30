

list_1=[16,9,8,-9,-13,9,6,-23,36]

list_2=[]
list_3=[]
for index in range (len(list_1)):
    if list_1[index]>0:
        list_2.append(list_1[index])
    else:
        list_3.append(list_1[index])

print(list_2)
print(list_3)
