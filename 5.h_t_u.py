#Ask for input
x = input("3 digit integer:")
#check if input is 3 digit
if not len(x) == 3:
    print("Please input a integer between 100 and 999")
#print result
print(x[0], "hundreds,", x[1], "tens, ", x[2], "units")