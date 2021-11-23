import math
from typing import DefaultDict

result = DefaultDict(lambda: 0)
revealed = set()

try:
    for org_num in reversed(range(0, 1000000, 210)):
        if org_num == 0:
            continue
        num = org_num
        i = 1
        count = 1
        if num not in revealed:
            for j in range(19):
                i = 1
                while i <= math.floor(num ** (1/2)) and i <= num:
                    if num % (i**2) == 0:
                        num = num // i
                        count += 1
                        revealed.add(num)
                    i += 1
            result[num] += count
        else:
            print("no")
        print(org_num)
    max_key = max(result, key=result.get)   
    print(max_key)
except KeyboardInterrupt:
    max_key = max(result, key=result.get)
    print(result, max_key)
    exit()