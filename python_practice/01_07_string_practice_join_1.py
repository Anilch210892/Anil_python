"""
# # Author Anilkumar
# # problem Statement:
# # input : India is my country and all indians are my brothers and sisters
"""
statement="India is my country and all indians are my" \
          " brothers and sisters "
statement_1 = statement.replace(" ","@")
print(statement_1)




statement5 ="India, officially the Republic of India, is a country in South Asia." \
            "It is the seventh largest country by area"

list_5 = statement5.split(" ")
print(list_5)





# str --> list
list_1 = statement.split(" ")
print(list_1)
# list --> str
statement= "##".join(list_1)
print(statement)

# find word brother index
index_find = statement.index("brother")
print(index_find)