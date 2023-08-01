"""author anilkumar
problem statement:
dictionary operations
"""

dict_5={"dhoni":"raina",
        "kohli":"pujara",
        "steven smith":"warner",
        "root":"stokes",
        "williamson":"latham",
        "cummins":"Ma starc",
        "aswin":"jadeja",
        "steyn":"morkel",
        "kohli":28,
        "kohli":12000,
        "smith":33,
        "root":29,
        "williamson":28}
x=dict_5["kohli"]
x=dict_5.get("steven smith")
print(x)
dict_5["root"]=["bairstow"]
x=dict_5.get("root")
print(x)


