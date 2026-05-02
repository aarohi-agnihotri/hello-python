distance = int(input("Enter distance: "))

if distance < 1:
    print("Please enter positive number!!")
    exit()
elif distance < 3:
    transport = "walk"
elif distance < 16:
    transport = "bike"
else:
    transport = "car"

print("Your mode of transportation is :", transport)