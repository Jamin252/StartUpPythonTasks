"""
def DPF(num):
    i = 1
    for j in range(19):
        i = 1
        while i <= math.floor(num ** (1/2)):
            if num % (i**2) == 0:
                num = num // i
            i += 1
    return num

x = []
for num in range(1000):
    if DPF(num) == num:
        x.append(num)
"""