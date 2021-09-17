"""
This is a function that only allow user to do caesar encryption
"""
x = str(input("String:").lower())
shift = int(input("shift number: "))
list = []
for i in range(shift, shift + 26):
    if i < 26:
        list.append(chr(65 + i))
    else:
        list.append(chr(65 + i - 26))
result = []
for count, key in enumerate(list):
    result.append((chr(97 + count), key))
for old, new in result:
    print(old, new)
    x = x.replace(old, new)
print(x.lower())
    