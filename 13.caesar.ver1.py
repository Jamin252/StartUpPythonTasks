#Ask for input
x = input("String:")

list = []
#Turn char in ascii code
for char in x:
    list.append(ord(char))

#convert
result = []
for num in list:
    if 65 <= num and num <=88:
        result.append(num + 2)
    elif num == 90 or num == 89:
        result.append(num - 24)
    elif 97 <= num and num <=120:
        result.append(num + 2)
    elif num == 121 or num == 122:
        result.append(num - 24)
    else:
        result.append(num)
#endfor

for i in result:
    print(chr(i), end="")
#endfor

## ACS Good iot works well but I can't see what yourporcess is. You need comments for that
