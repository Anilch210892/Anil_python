# it a negation operation
# True becomes False and False become true

result = True
if not result:
    print("Hello")
else:
    print("Hello1")

# we can override same variable mulitple times
result = (9==9)
result_1 = ("hi"==9)
result_2 = (9.0==9)

if not (result or result_2) and result_1:
    print("Hello4")
else:
    print("Hello5")