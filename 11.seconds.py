#Ask for input
x = input("time:")

#split
list = x.split(":")

#print
print(str(int(list[0]) * 3600 + int(list[1]) * 60 + int(list[2])), "seconds")