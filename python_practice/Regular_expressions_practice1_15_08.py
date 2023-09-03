

import re
input_string = r"This is pycharm .ide This 9 is 456 mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1"

pattern = re.compile(r"[^a-zA-Z0-9]")
matches = pattern.finditer(input_string)
print(matches)
for i in matches:
    print(i)

matches = pattern.findall(input_string)
print(matches)

matches = pattern.search(input_string)
print(matches)








