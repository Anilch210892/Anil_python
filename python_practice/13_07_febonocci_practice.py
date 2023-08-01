

a=0
b=1
x=int(input("Enter the value of x:"))
list_1=[a,b]
for number in range(0,x-2):
    c=a+b
    a=b
    b=c
    #list_1.append(c) must be with in the loop, should not be outside the for loop
    list_1.append(c)
print(f"The final list is:{list_1}")
