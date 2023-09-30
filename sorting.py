

# sorting elements in the list

list_1=[5,9,18,20,35,52]
for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[i]>list_1[j]:
            list_1[i],list_1[j]=list_1[j],list_1[i]
print(list_1)
