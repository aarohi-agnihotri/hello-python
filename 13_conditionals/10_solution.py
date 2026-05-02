species = input("Enter your pet's species: ").lower()
age = int(input("Enter your pet's age: "))

if age < 0:
    print("Please enter valid age!")
    exit()

if species == "dog":
    if age < 2:
        print("Give them puppy food")
    elif age <= 5:
        print("Give them adult dog food")
    elif age <= 20:
        print("Give them senior dog food")
    else:
        print("Enter valid dog's age!!")
elif species == "cat":
    if age < 2:
        print("Give them kitten food")
    elif age <= 5:
        print("Give them adult cat food")
    elif age <= 20:
        print("Give them senior cat food")
    else:
        print("Enter valid cat's age!!")
else:
    print("Food recommendation about", species, "isn't available")
