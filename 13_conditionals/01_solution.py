# age = 25 - direct enter

age = int(input("enter your age \n")) 
# print(type(age))

# age = input("Enter your age : \n") #input from user on cmd/terminal
# age_in_int = int(age) # explicit convert into int

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult")
else:
    print("senior")