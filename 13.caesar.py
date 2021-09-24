"""
This is a function that only allow user to do caesar encryption
"""
#Ask for shift and the string
x = str(input("String:").lower())
shift = int(input("shift number: "))

#make a altered list
list = []

for i in range(shift, shift + 26):
    if i < 26:
        list.append(chr(65 + i))
    else:
        list.append(chr(65 + i - 26))
result = []

#append the new key with its corresponding ABCD
for count, key in enumerate(list):
    result.append((chr(97 + count), key))

#replace the old key with the new key
for old, new in result:
    print(old, new)
    x = x.replace(old, new)
#Print the new key
print(x.lower())
    