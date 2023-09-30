


list_2=[1,15,18,9,6,-3]
for i in range(len(list_2)):
    for j in range(len(list_2)):
        if list_2[i]<list_2[j]:
            list_2[i],list_2[j]=list_2[j],list_2[i]

print(list_2)
print(list_2[-1])
print(list_2[-2])
print(list_2[-3])




average_1=sum(list_2)/len(list_2)
print(average_1)



average_2 = (list_2[-1]+list_2[-2])/2
print(average_2)



average_3 = (list_2[-1]+list_2[-2]+list_2[-3])/3
print(average_3)
"""



















"""

