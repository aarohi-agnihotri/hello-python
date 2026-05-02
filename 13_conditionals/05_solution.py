weather = input("Enter today's weather (sunny, rainy or snowy): ").lower()

if weather == "sunny":
        print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Please enter weather from given choices")
