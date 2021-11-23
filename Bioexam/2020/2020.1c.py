"""
Answer is IIIX
"""


SPECIAL = {4: "IV", 9: "IX", 40: "XL",90: "XC", 400:"CD", 900:"CM"}


def main(string):
    temp_result = []
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
            if item in SPECIAL:
                newstring = newstring + SPECIAL[item]
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
            try:
                newstring += item
            except TypeError:
                print(item, temp_result, "string = ", string)
                exit()
    return newstring


if __name__ == "__main__":
    result = []
    count = 0
    for i in range(1,4000):
        print(i)
        newstring = ""
        if i in SPECIAL:
            newstring = newstring + SPECIAL[i]
        else:
            m = i // 1000
            i = i % 1000
            d = i // 500
            i %= 500
            c = i // 100
            i %= 100
            l = i // 50
            i %= 50
            x = i // 10
            i %= 10
            v = i // 5
            i %= 5
            i_i = i
            newstring = newstring + "M" * m + "D" * d + "C" * c + "L" * l + "X" * x + "V" * v + "I" *i_i
        print(newstring)
        temp = main(newstring)
        if temp not in result:
            count +=1
            result.append(temp)
    print(len(result))