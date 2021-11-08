import time
start = time.time()
def temp(num):
    if num == 0 or num == 1:
        return num
x = int(input("NUM: "))
start = time.time()
temp(x)
print(time.time() - start)
start1 = time.time()
time.sleep(1)
print(time.time() - start1)