number = int(input("enter a number: "))

# --------regular fucntion--------
# def cube(number):
#     return number ** 3

# --------LAMBDA FUNCTION---------
cube = lambda number : number ** 3
print("Cube of", number, ":", cube(number))