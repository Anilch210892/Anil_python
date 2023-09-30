
def countcharcters(input_string):
    capital_letters=0
    small_letters=0
    special_charcters=0
    numbers=0
    for charcter_1 in input_string:
        if charcter_1.isupper():
            # check ASCII values for uppercase
            capital_letters+=1
        elif charcter_1.islower():
            # check ASCII values for lowercase
            small_letters+=1

        elif 33<=ord(charcter_1)<=47 or 58<=ord(charcter_1)<=64 or 91<=ord(charcter_1)<=96 :
            special_charcters+=1

        elif 48<=ord(charcter_1)<=57:
            numbers+=1

        else:
            numbers+=1