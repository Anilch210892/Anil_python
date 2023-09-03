# backslash mentions special character

# \n \t has support, \y not supported.
print("Hi I am Raviteja \\n son of Umamaheswrarao")
print("Hi I am Raviteja \y son of Umamaheswrarao")

print("Hi I am Raviteja \n son of Umamaheswrarao")


print(r"Hi I am Raviteja \\n son of Umamaheswrarao")
print(r"Hi I am Raviteja \n son of Umamaheswrarao")

# we can use in combination with -fr
hi =2
print(fr"Hi I am Raviteja \n son of Umamaheswrarao {hi}")

# autoqotation generator by default
print("India is my country and all Indians are my brothers and sisters. "
      "I love my country and I am proud of its rich and varied heritage. "
      "I shall always strive to be worthy of it. I shall give respect to my parents, "
      "teachers and elders and treat everyone with courtesy.")

var_1 = 9

# backslash at the end of the line indiactes extension of the line
if var_1>9 and var_1>10 and var_1>9 and var_1>10 and var_1>9 and var_1>10 and var_1>9 and var_1>10 and var_1>9 and \
    var_1>10 and var_1>9 and var_1>10 and var_1>9 and var_1>10 and var_1>9 and var_1>10 :
    pass