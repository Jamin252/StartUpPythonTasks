#Ask string
str = input("String:")
text = []
result = ""
for char in str:
    text.insert(0, char)
for var in text:
    result +=var
print(result)