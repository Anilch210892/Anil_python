# rectangle area
length = input("Enter length")
width = input("Enter width")

assert type(length) == str
assert type(width) == str

length = int(length)
width = int(width)

assert length!=0,"length  should NOT be zero"
assert width!=0,"width  should NOT be zero"

print(f"area is {length*width}")