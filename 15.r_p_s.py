import random
#Ask for input
x = input("Rock Paper Scissor:(R/P/S)")

#Check for input
if x !="R" and x !="P" and x !="S":
    print("Use R(rock), P(paper), S(scissor)")
    exit()

#Generate random number
temp = str(random.randint(1,3))
y = temp
for o,n in [("R", "1"), ("P", "2"), ("S", "3")]:
    x = x.replace(o,n)
    y = y.replace(n,o)
#endfor
result = int(x) - int(temp)
if result == -2 or result == 1:
    print("Win")
elif result == 0:
    print("Draw")
elif result == -1 or result == 2:
    print("lose")
#endif
print(y)