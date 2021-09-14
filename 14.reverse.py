#Ask string
str = input("String:")
text = []
result = ""
#Insert charater into the front
for char in str:
    text.insert(0, char)
#endfor

for var in text:
    print(var, end="")
#endfor