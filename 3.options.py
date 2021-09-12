#Set ans variable
ans = ""
#Ask for a number until user input 1 to 3
while str(ans) != "1" and str(ans) != "2" and str(ans) != "3":
    ans = input("From 1 to 3, please choose a number:")
#print the option user chose
print(f"You have selected option number {ans}")