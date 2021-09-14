#Set ans variable
ans = int()
#Ask for a number until user input 1 to 3
while not 0 < ans < 4:
    ans = int(input("From 1 to 3, please choose a number:"))
#endwhile

#print the option user chose
print(f"You have selected option number {ans}")

## ACS Might have been better to use the integer version then
## ACS you can use the < and > comparison operators?? 
## ACS - If you had 100 options it would be tricky!