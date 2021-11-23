def func(x, y):

    k = 1
    while True:
        if abs(k * x - k * y) % 1440 == 0:
            return k
        k += 1
max_x = 0
max_y = 0
max_value = 0

for i in range(60):
    for j in range(60):
        temp = func(i, j)
        if temp > max_value:
            max_value = temp
            max_x = i
            max_y = j
print(max_value)