#Ask for password
password = input("password:")
#Check if password length is more than 6
if len(password) > 6:
    print("Password is valid")
else:
    print("Password is invalid")