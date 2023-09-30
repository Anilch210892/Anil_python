


list_2=[1,15,18,9,6,-3]
for i in range(len(list_2)):
    for j in range(len(list_2)):
        if list_2[i]<list_2[j]:
            list_2[i],list_2[j]=list_2[j],list_2[i]

print(list_2)