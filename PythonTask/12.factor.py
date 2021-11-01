#Ask input
x = input("integer:")
x = int(x)

#find factor
list = []
for i in range(1, x):
    if x % i == 0:
        list.append(i)
#endfor

for u in list:
    if u == list[-1]:
        print(u)
        exit()
    print(u, end=", ")
#endfor

# ACs Good but it misses out the number itself .. e,.g. has 48 as a factor. 
## There are some comments but your algorithm isn't really described! How does this work?