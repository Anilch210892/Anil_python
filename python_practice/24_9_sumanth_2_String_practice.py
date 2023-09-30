
"""
input_string="anil kumar is a software engineer"

a position is odd then print that word
if a position is even position then word is not printed

"""
list_1=[]
input_string="anil kumar is a software engineer"
list_1 = input_string.split()
for word in list_1:
    #if word.find("a")%2==1:
    if word.find("a")%2!=0 and "a" in word:
        print(word)















































