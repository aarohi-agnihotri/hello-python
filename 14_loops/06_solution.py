number = int(input("enter a number: "))
factorial = 1

# ======First method=========
while number > 0:
    factorial *= number
    number -= 1

# ======second method=========
# for i in range(1, number+1):
#     factorial *= i

print("Factorial of :", factorial)