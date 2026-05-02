fruit = input("enter fruit name : ").lower()

if fruit == "banana":
    fruit_color = input(f"enter color of {fruit} - (green, yellow or brown) : ").lower()
    if fruit_color == "green":
        print(fruit, "is unripe")
    elif fruit_color == "yellow":
        print(fruit, "is ripe")
    elif fruit_color == "brown":
        print(fruit, "is overripe")
    else:
        print("wrong color entered")

elif fruit == "apple":
    fruit_color = input(f"enter color of {fruit} - (green or red) : ").lower()
    if fruit_color == "green":
        print(fruit, "is unripe")
    elif fruit_color == "red":
        print(fruit, "is ripe")
    else:
        print("wrong color entered")
else:
    print(f"I don't have information about {fruit}")