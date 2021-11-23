x = input("input: ").split(" ")
string= x[0]
step = x[1]
temp_result = []
special = {4: "IV", 9: "IX", 40: "XL",90: "XC", 400:"CD", 900:"CM"}
for i in range(int(step)):
    temp_result = []
    temp = None
    count = 1
    for char in string:
        if temp == None:
            temp = char
        elif temp == char:
            count +=1
        else:
            temp_result.append(count)
            temp_result.append(temp)
            count = 1
            temp = char
    temp_result.append(count)
    temp_result.append(temp)
    newstring = ""
    for item in temp_result:
        if isinstance(item, int):
            if item in special:
                newstring = newstring + special[item]
            else:
                m = item // 1000
                item = item % 1000
                d = item // 500
                item %= 500
                c = item // 100
                item %= 100
                l = item // 50
                item %= 50
                x = item // 10
                item %= 10
                v = item // 5
                item %= 5
                i = item
                newstring = newstring + "M" * m + "D" * d + "C" * c + "L" * l + "X" * x + "V" * v + "I" *i
        else:
            newstring += item
    string = newstring
print(string.count("I"), string.count("V"))