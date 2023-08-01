"""author anilkumar
problem statement:
set  operations
"""

myset_2={"ab",8,25,0.6,"jnm",100,"yz","dcm","jkg",185}
print(myset_2)

print(len(myset_2))
print("ab"in myset_2)
print("289"in myset_2)

myset_3={"ab","hnop",10,20,0.2,"jnm",500,100,"yz","jkg",185}
myset_2.update(myset_3)
print(myset_2)

myset_2={"ab",8,25,0.6,"jnm",100,"yz","dcm","jkg",185}
myset_2.remove(100)
myset_2.remove("dcm")
print(myset_2)

myset_2.remove("yhu")
print(myset_2)

myset_2.discard("yhu")
print(myset_2)


