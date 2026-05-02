password = input("Enter password : ")
password_len = len(password)

if password_len <= 5:
    print("Weak password, try again")
elif password_len <= 10:
    print ("Make it strong")
else:
    print ("Finally, you made it strong")
