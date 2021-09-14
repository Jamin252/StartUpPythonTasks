#Ask for two integer:
x = input("integer:")
y = input("integer:")

if not x.isdigit() or not y.isdigit:
    print("please input a integer")
    exit()
#endif
x = int(x)
y = int(y)

if x > y:
    print(str(x)+","+str(y))
elif y > x:
    print(str(y)+","+str(x))
else:
    print("same number")
#endif