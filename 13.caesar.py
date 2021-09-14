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
    elif 97 <= num and num <=170:
        result.append(num + 2)
    elif num == 171 or num == 172:
        result.append(num - 24)
    else:
        result.append(num)
#endfor

for i in result:
    print(chr(i), end="")
#endfor
