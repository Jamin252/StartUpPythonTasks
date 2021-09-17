def main():
    #Ask for a string
    x = str(input("String:").lower())
    #Ask for type of encryption
    choice = input("shift or key: ")
    if choice == "shift":
        result = caesar()
    else:
        result = sub()
    print(x)
    print(result)

    #replace the old char with the key
    for old, new in result:
        print(old, new)
        x = x.replace(old, new)
    print(x.lower())
    return
    
#Caesar encryption
def caesar():
    try:
        shift = int(input("shift number: "))
    except ValueError:
        print("please enter a integer from 0 to 26")
        exit()
    list = []
    #Make the caesar key
    for i in range(shift, shift + 26):
        if i < 26:
            list.append(chr(65 + i))
        else:
            list.append(chr(65 + i - 26))
    result = []
    #Match a to z to the caesar key
    for count, key in enumerate(list):
        result.append((chr(97 + count), key))
    return result

#Substitution encryption
def sub():
    #Get the key
    keys = input("key: ").upper()
    if len(keys) != 26:
        print("please enter a valid key")
        exit()
    result = []
    #Match a to z to the key
    for count, key in enumerate(keys):
        result.append((chr(97 + count), key))
    return result

if __name__ == "__main__":
    main()
