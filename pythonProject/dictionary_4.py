"""author anilkumar
problem statement:
dictionary operations
"""
cartype={"brand":"maruthi",
         "model":"swift",
         "year of manufacture":2018,
         "colour":["red","green","white"]
        }
x=cartype["brand"]
print(x)
x=cartype.get("year of manufacture")
print(x)
cartype["model"]="landrover"
x=cartype.get("model")
print(x)


