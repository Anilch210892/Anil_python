"""
# # Author Anilkumar
# # problem Statement:
# # input :
   output :
"""

"""

def addition (a,b,c=0,d=0):
    return a+b+c+d
print(addition(2,3))

print(addition(2,3,4))

print(addition(2,3,4,5))

"""



"""
# addition(2,3,4,5,6)
# TypeError: addition() takes from 2 to 4 positional arguments but 5 were given

print(addition(2,3,4,5,6))

"""



def charminar_visit_fees(name,age,indian_nation=True):
    if indian_nation:
        fees=100
        return(f"visitor name is {name},age is {age} and fees is {fees}")
    else:
        fees=1000
        return (f"visitor name is {name},age is {age} and fees is {fees}")
var_1 = charminar_visit_fees("Ravi",29)
var_2 = charminar_visit_fees("Andrew",91,False)
var_3 = charminar_visit_fees("Anil",30,True)
print(var_1)
print(var_2)
print(var_3)






