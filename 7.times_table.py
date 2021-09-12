#Ask for integer
x = input("integer from 1 to 10:")

#check if it is an integer
if not x.isdigit():
    print("please input a integer")
    exit()
x = int(x)
#print
for i in range(x, x * 10 + 1, x):
    print(i)