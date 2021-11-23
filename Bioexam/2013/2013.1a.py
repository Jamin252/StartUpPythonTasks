temp = input("Time: ").split(" ")
x = int(temp[0])
y = int(temp[1])

k = 1
while True:
    if abs(k * x - k * y) % 1440 == 0:
        temp1 = k*x % 1440
        hour = str(temp1 // 60)
        mins = str(temp1 % 60)
        print(hour+":"+mins)
        exit()
    k += 1