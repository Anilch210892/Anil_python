# overridable is changing the entire value
# mutable is chnaging partial portion
list_1 = [1,2,34.6]
# overridable
list_1[2]=31.2
list_1 = "Anil"
# mutable
print(list_1)

dict_1 = {1:"one",2:"Two"}
# overridable
dict_1[2]="Three"
# mutable
dict_1 = {1:"one",2:"Two"}
print(dict_1)

tuple_1 = (1,3,4)
# overridable
tuple_1 = (1,3,14)
# immutable
# tuple_1[2]=56
# print(tuple_1)
#     tuple_1[2]=56
#     ~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment


string_1 = "Hello"
# overridable
string_1 = "Hello123"
# immutable
# string_1[1]="z"
# print(string_1)
#     string_1[1]="z"
#     ~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment


