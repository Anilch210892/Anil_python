"""
# # Author Anilkumar
# # problem Statement:
# # input :
   output :
"""





#using normal approach
"""

list_2 = []
for i_var in range(10):
    list_2.append(i_var)
print(list_2)

"""



#using comprehension
"""

list_2 = [i_var for i_var in range(10) if True]
print(list_2)

"""




"""
list_3=[]
for i_var in range(3,33,3):
    list_3.append(i_var)
print(list_3)
"""



"""
list_4=[]
for i_var in range(31):
    if i_var%3==0:
        list_4.append(i_var)
print(list_4)
"""


list_4 = [i_var for i_var in range(10) if i_var%3==0]
print(f"list_4 value is {list_4}")





set_2 = set()
for i_var in range(10):
    set_2.add(i_var)
print(f"set_2 value is {set_2}")


set_4 = {i_var for i_var in range(10) if i_var%3==0}
print(f"set_4 value is {set_4}")


list_6 = [i_var**3 for i_var in range(6) if True]
print(list_6)


#anil19@@@ 1 4 09 16 25 doubts
"""
list_5 = [1,9,8,245]
list_7 = [list_5[i_var]**2 for i_var in range(len(list_5)) if True]
print(list_7)

"""

list













