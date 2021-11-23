"""
Distinct Prime Factorisation
"""
import math
#Ask for a number
num = int(input("Number: "))


i = 1
for j in range(6):
    i = 1
    while i <= math.floor(num ** (1/2)):
        if num % (i**2) == 0:
            num = num // i
        i += 1
print(num)