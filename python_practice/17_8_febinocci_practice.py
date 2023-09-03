

a=0
b=1
c=int(input("Enter the febinocci number c:"))
list_1=[a,b]
for number in range(0,c-2):
    c=a+b
    a=b
    b=c
    list_1.append(c)
print(f"the final value of the list_1 is {list_1} ")