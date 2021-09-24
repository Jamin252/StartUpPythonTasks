#Ask for string
string = input("Sentencce:")

#Strip leading and trailing whitespace
string = string.strip()

#Find number of space
result = string.count(" ") + 1

#Print answer
print(result)

## ACS This works providing there is just one space between thew words. Good