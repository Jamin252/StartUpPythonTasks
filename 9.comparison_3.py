#ask for 3 integer
x = input("integer:")
y = input("integer:")
z = input("integer:")

#Sort from highest to lowest
list = [x, y, z]
list.sort(reverse=True)

#Print
print(list[0]+", "+list[1]+", "+list[2])