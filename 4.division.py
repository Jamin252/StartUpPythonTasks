#Ask for integer
inte = input("integer:")

#Check if input is an integer
if not inte.isdigit():
    print("please input a integer")
    exit()
#endif
inte = int(inte)

#Ask for divisor
di = input("devisor:")

#Check if input is an integer
if not di.isdigit():
    print("please input a integer")
    exit()
#endif

di = int(di)

#print result
print(str(inte // di) , "remainder" , str(inte % di))

##ACS - Good the code works and you have thought about some error trpping
## ACS Need more comments at the end of constructs!