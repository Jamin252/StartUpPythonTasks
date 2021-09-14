#Set ans variable
ans = ""
#Ask for a number until user input 1 to 3
while str(ans) != "1" and str(ans) != "2" and str(ans) != "3":
    ans = input("From 1 to 3, please choose a number:")
#print the option user chose
print(f"You have selected option number {ans}")

## ACS Might have been better to use the integer version then
## ACS you can use the < and > comparison operators?? 
## ACS - If you had 100 options it would be tricky!