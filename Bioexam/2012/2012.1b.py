#10, 20, 40, 50, 80, 100, 160, 200, 250,320"""
import math
#Ask for a number

list = []
org_num = 1
i = 1
while len(list) < 10:
    num = org_num
    for j in range(19):
        i = 1
        while i <= math.floor(num ** (1/2)):
            if num % (i**2) == 0:
                num = num // i
            i += 1
    if num == 10:
        list.append(org_num)
    org_num += 1
print(list)
